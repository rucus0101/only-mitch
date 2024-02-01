import argparse
import argcomplete
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_cli
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


def run_a_command_list(task: Task, cmds_and_dirnames: list):
    result = task.run(
        task=napalm_cli,
        commands=[cmd[0] for cmd in cmds_and_dirnames]
    )
    # write a command output to a file
    for cmd, cmd_dirname in cmds_and_dirnames:
        task.run(
            task=write_file,
            content=result.result[cmd],
            filename=f'{cmd_dirname}/{task.host}.txt'
        )
        print('Saved ' + f'{cmd_dirname}/{task.host}.txt')


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
    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    # create the required directories outside Nornir to avoid issues with threading
    # check if test directory exists
    test_dir_name = f'eantc{args.year}/testbeds/{args.inventory}/tests/{args.task}'
    test_dir_full_path = os.path.join(os.getcwd(), test_dir_name)
    if not os.path.isdir(test_dir_full_path):
        sys.exit(f'ERROR: {test_dir_full_path} does not exist!')
    # build time stamp if required
    if args.no_timestamp:
        current_time = ''
    else:
        current_time = time_stamp()
    # create config dir
    if current_time:
        config_dir = os.path.join(test_dir_full_path, f'configs_{current_time}')
    else:
        config_dir = os.path.join(test_dir_full_path, f'configs')
    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)
    # create outpit dir for test commands
    if current_time:
        test_out_dir = os.path.join(test_dir_full_path, f'test_results_{current_time}')
    else:
        test_out_dir = os.path.join(test_dir_full_path, f'test_results')
    if not os.path.isdir(test_out_dir):
        os.makedirs(test_out_dir)

    # build a list of show commands
    snapshot_command_list = list()
    with open(f'{test_dir_full_path}/test-commands.txt', 'r') as snapshot_commands_file:
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

    # init Nornir
    nr = InitNornir(
        runner={'plugin': 'threaded', 'options': {'num_workers': 20}},
        inventory={
            'plugin': 'SimpleInventory',
            'options': {
                'host_file': f'{os.getcwd()}/eantc2024/testbeds/evpn-vxlan/nornir-hosts.yml',
                'group_file': f'{os.getcwd()}/nornir-groups.yml',
                'defaults_file': f'{os.getcwd()}/nornir-defaults.yml'
            }
        }
    )
    
    # collect configs
    result = nr.run(task=get_config, cfg_dir=config_dir)
    if result.failed:
        print(f'ERROR: Failed to collect configs from the following hosts: {[k for k in result.failed_hosts.keys()]}')
    # collect show comands
    result = nr.run(task=run_a_command_list, cmds_and_dirnames=cmd_list_with_dirnames)
    if result.failed:
        print(f'ERROR: Failed to collect show commands from the following hosts: {[k for k in result.failed_hosts.keys()]}')
