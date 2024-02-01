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
from run.tools import time_stamp


def get_config(task: Task, test_dir_full_path: str, current_time='') -> Result:
    if current_time:
        out_dir = os.path.join(test_dir_full_path, f'configs_{current_time}')
    else:
        out_dir = os.path.join(test_dir_full_path, f'configs')
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    result = task.run(
        task=napalm_get,
        getters=['config']
    )
    task.run(
        task=write_file,
        content=result.result['config']['running'],
        filename=f'{out_dir}/{task.host}.cfg'
    )
    print('Saved ' + f'configs/{task.host}.cfg')


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
    
    # check if test directory exists
    test_dir_name = f'eantc{args.year}/testbeds/{args.inventory}/tests/{args.task}'
    test_dir_full_path = os.path.join(os.getcwd(), test_dir_name)
    if not os.path.isdir(test_dir_full_path):
        sys.exit(f'ERROR: {test_dir_full_path} does not exist!')
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
    # current time must be set outside of Nornir task to have single time stamp
    if args.no_timestamp:
        current_time = ''
    else:
        current_time = time_stamp()
    # collect configs
    result = nr.run(task=get_config, test_dir_full_path=test_dir_full_path, current_time=current_time)
    if result.failed:
        print(f'ERROR: Failed to collect configs from the following hosts: {[k for k in result.failed_hosts.keys()]}')
