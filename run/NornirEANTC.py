from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_cli
import os
import sys


class Otnorok:

    def __init__(self):
        self.nr = InitNornir(
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
