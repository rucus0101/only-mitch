# eantc-automation

This repository is under construction and not yet fully functional.

To start Containerlab:

- Place cEOS-lab image to `.gitignored`
- Import the image: `docker import .gitignored/<cEOS-archive-filename> ceos-lab:latest`
- Start the lab: `make start`
- To stop the lab: `make stop`

To install `run` CLI:

- `pip3 install  --force file://$(pwd)`
- `eval "$(register-python-argcomplete run)"`

Test the CLI without install:

- `python3 -m run --help`
