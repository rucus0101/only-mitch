import argparse
import argcomplete
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_cli, napalm_configure
from nornir.core.task import Task, Result
import os
import sys
import re
from run.tools import time_stamp


def get_config(task: Task, cfg_dir: str) -> Result:
    result = task.run(
        task=napalm_get,
        getters=['config']
    )
    task.run(
        task=write_file,
        content=result.result['config']['running'],
        filename=f'{cfg_dir}/{task.host}.cfg'
    )
    print('Saved ' + f'configs/{task.host}.cfg')


def run_a_command_list(task: Task, cmds_and_dirnames: list) -> Result:
    result = task.run(
        task=napalm_cli,
        commands=[cmd[0] for cmd in cmds_and_dirnames]
    )
    # generate a single report file with all commands
    report_string = f'# Test results for {task.host}\n\n'
    for cmd, cmd_dirname in cmds_and_dirnames:
        report_string += f'## {cmd}\n\n'
        report_string += f'```text\n{result.result[cmd]}```\n\n'
        task.run(
            task=write_file,
            content=report_string,
            filename=f'{os.path.dirname(cmd_dirname)}/{task.host}_merged.md'
        )
        print('Saved ' + f'{os.path.dirname(cmd_dirname)}/{task.host}_merged.md')
    # write a command output to a file
    for cmd, cmd_dirname in cmds_and_dirnames:
        task.run(
            task=write_file,
            content=result.result[cmd],
            filename=f'{cmd_dirname}/{task.host}.txt'
        )
        print('Saved ' + f'{cmd_dirname}/{task.host}.txt')


def get_sh_tech(task: Task, tech_dir: str) -> Result:
    result = task.run(
        task=napalm_cli,
        # remove any non-printable characters, otherwise task may fail
        commands=['show tech-support | no-more | tr -cd "[:print:][:space:]"']
    )
    task.run(
        task=write_file,
        content=result.result['show tech-support | no-more | tr -cd "[:print:][:space:]"'],
        filename=f'{tech_dir}/{task.host}.txt'
    )
    print('Saved ' + f'{tech_dir}/{task.host}.txt')


def recover_config(task: Task, cfg_dir: str, dry_run: bool) -> Result:
    result = task.run(
        task=napalm_configure,
        replace=True,
        filename=f'{cfg_dir}/{task.host}.cfg',
        dry_run=dry_run
    )
    if dry_run:
        print_result(result)
    else:
        print(f'Recovered {task.host} config from {cfg_dir}/{task.host}.cfg')
    return result


def interpreter():
    # Get cookiecutter output_directory from CLI argument or default
    parser = argparse.ArgumentParser(
        prog="run",
        description="A simple CLI tool to run EANTC tests", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-y', '--year', default=2024,
        help='The EANTC year. Optional, default is 2024. This will be used to find tests parent directory.'
    )
    parser.add_argument(
        '-i', '--inventory', choices=['evpn-vxlan', 'evpn-mpls', 'sr-mpls'], required=True,
        help='EANTC test inventory: [ evpn-vxlan, evpn-mpls, sr-mpls ]. Required!'
    )
    parser.add_argument(
        '-t', '--task', default='',
        # help="Task to perform on the selected EANTC inventory: "
        help = "test\ntest"
    )
    parser.add_argument(
        '-notime', '--no_timestamp', action='store_true', default=False,
        help='Do not add time stamp to the output directory name. By default it will be added.'
    )
    parser.add_argument(
        '-r', '--recover', default='',
        help='Recover device configuration from the specified directory. Please provide the full path to the directory as an argument.'
    )
    parser.add_argument(
        '-ndr', '--no_dry_run', action='store_false', default=True,
        help='Do not recover configs, use Nornir dry run to check the diff.'
    )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    # overwrite default settings if custom settings defined in .gitignored
    nr_defaults_file = f'{os.getcwd()}/.gitignored/nornir-defaults.yml'
    if not os.path.isfile(nr_defaults_file):
        nr_defaults_file = f'{os.getcwd()}/nornir-defaults.yml'
    nr_groups_file = f'{os.getcwd()}/.gitignored/nornir-groups.yml'
    if not os.path.isfile(nr_groups_file):
        nr_groups_file = f'{os.getcwd()}/nornir-groups.yml'
    # init Nornir
    nr = InitNornir(
        runner={'plugin': 'threaded', 'options': {'num_workers': 20}},
        inventory={
            'plugin': 'SimpleInventory',
            'options': {
                'host_file': f'{os.getcwd()}/eantc2024/testbeds/{args.inventory}/nornir-hosts.yml',
                'group_file': f'{os.getcwd()}/nornir-groups.yml',
                'defaults_file': nr_defaults_file
            }
        }
    )

    if args.recover:
        if not os.path.isdir(args.recover):
            sys.exit(f'ERROR: {args.recover} directory does not exist! Must be a full path!')
        result = nr.run(task=recover_config, cfg_dir=args.recover, dry_run=args.no_dry_run)
        if result.failed:
            print(f'ERROR: Failed to recover config on: {[k for k in result.failed_hosts.keys()]}')
    else:

        # build time stamp if required
        if args.no_timestamp:
            time_stamp_string = ''
        else:
            time_stamp_string = f'_{time_stamp()}'

        # create the required directories outside Nornir to avoid issues with threading
        base_dir = os.path.join(os.getcwd(), f'eantc{args.year}/testbeds/{args.inventory}/tests')
        if args.task == 'tech':
            sub_dir = base_dir
        else:
            sub_dir = os.path.join(base_dir, args.task)
        if not os.path.isdir(sub_dir):
            sys.exit(f'ERROR: {sub_dir} does not exist!')
        if args.task == 'tech':
            tech_support_dir = os.path.join(sub_dir, f'tech_support{time_stamp_string}')
            if not os.path.isdir(tech_support_dir):
                os.makedirs(tech_support_dir)
            # collect show tech
            result = nr.run(task=get_sh_tech, tech_dir=tech_support_dir)
            if result.failed:
                print(f'ERROR: Failed to collect show tech from the following hosts: {[k for k in result.failed_hosts.keys()]}')
        else:
            config_dir = os.path.join(sub_dir, f'configs{time_stamp_string}')
            if not os.path.isdir(config_dir):
                os.makedirs(config_dir)
            test_out_dir = os.path.join(sub_dir, f'test_results{time_stamp_string}')
            if not os.path.isdir(test_out_dir):
                os.makedirs(test_out_dir)
    
            # build a list of show commands
            snapshot_command_list = list()
            with open(f'{sub_dir}/test-commands.txt', 'r') as snapshot_commands_file:
                snapshot_command_list = [a_line.strip() for a_line in snapshot_commands_file]

            cmd_list_with_dirnames = list()
            for a_command in snapshot_command_list:
                # find all words in a command to remove all non-printable characters
                word_list = re.findall(r"[\w]+", a_command)
                # build prefix for a show command to be added to the filename or directory name
                cmd_line = ''
                while word_list:
                    cmd_line += word_list.pop(0)
                    if word_list:  # if not the last word, add separator
                        cmd_line += '-'
                cmd_list_with_dirnames.append((a_command, os.path.join(test_out_dir, cmd_line)))
                # create subdirectory for cli command to be collected
                cmd_out_dir = os.path.join(test_out_dir, cmd_line)
                if not os.path.isdir(cmd_out_dir):
                    os.makedirs(cmd_out_dir)

            # collect configs
            result = nr.run(task=get_config, cfg_dir=config_dir)
            if result.failed:
                print(f'ERROR: Failed to collect configs from the following hosts: {[k for k in result.failed_hosts.keys()]}')
            # collect show commands
            result = nr.run(task=run_a_command_list, cmds_and_dirnames=cmd_list_with_dirnames)
            if result.failed:
                print(f'ERROR: Failed to collect show commands from the following hosts: {[k for k in result.failed_hosts.keys()]}')
