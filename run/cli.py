import argparse
import argcomplete
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_cli
import os
import sys
from run.tools import time_stamp


def get_config(task, test_dir_full_path):
    out_dir = os.path.join(test_dir_full_path, f'configs_{time_stamp}')
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
    # collect confirs
    nr.run(task=get_config)
