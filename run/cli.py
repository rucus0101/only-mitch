import argparse
import argcomplete


def interpreter():
    # Get cookiecutter output_directory from CLI argument or default
    parser = argparse.ArgumentParser(
        prog="run",
        description="A simple CLI tool to run EANTC tests")
    parser.add_argument(
        '-y', '--year', default=2024,
        help='The EANTC year. Optional, default is 2024. This will be used to find tests parent directory.'
    )
    parser.add_argument(
        '-c', '--category', default='',
        help='EANTC test category: evpn-vxlan, evpn-mpls, sr-mpls'
    )
    parser.add_argument(
        '-t', '--test', default='',
        help="EANTC test name in the category: 1.0, 1.1, etc."
    )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
