# eantc-automation

## How to Get Support

This README only provides the most essential info. It will not be complete due to the time constraints.  
Please watch the video recording explaining the EANTC test workflow or ask questions.

For any questions before or during EANTC event please contact:

- Petr Ankudinov < [pa@arista.com](pa@arista.com) >
- Mitch Vaughan < [mitch@arista.com](mitch@arista.com) >

## How to start

### Install Nornir and `run` tool

> **NOTE**: There is no need to run `eval` or `pip3 install` when using `run` CLI inside VSCode dev container. It's part of the dev container build process.

To install `run` CLI:

- Clone this Github repository and make it your working directory
- `pip3 install --force file://$(pwd)`
- `eval "$(register-python-argcomplete run)"`

It is also possible to install `run` CLI tool from the Github repository directly, without cloning it:

- `pip3 install --force git+https://github.com/arista-netdevops-community/eantc-automation.git`
- `eval "$(register-python-argcomplete run)"`

Test the CLI without install:

- `python3 -m run --help`

### Start Containerlab

To start Containerlab:

- Place cEOS-lab image to `.gitignored`
- Import the image: `docker import .gitignored/<cEOS-archive-filename> ceos-lab:latest`
- Start the lab: `make start`
- To stop the lab: `make stop`

Containerlab is only required to test Nornir `run` CLI before the event.  
During the event the inventory must point to physical devices.

## How to Use `run` CLI

1. Fork the repository, clone it to your machine and open in VSCode dev container (or install the `run` tool locally using `venv` or `pyenv`).
2. Create a new branch for your tests.
3. Make sure that your `nornir-defaults.yml` has correct credentials. This tool is not providing any secure way to store the credentials, but you can create copy of `nornir-defaults.yml` in the `.gitignored/` directory and set the real password there. This will avoid committing and pushing the password to Github. If defined in `.gitignored/`, `nornir-defaults.yml` and `nornir-groups.yml` will take precedence over files in the repository root.
4. Create a test inventory structure on top of existing template. For example:

    ```text
    eantc2024
    |- testbeds
    |- sr-mpls
    |- evpn-mpls
    |- evpn-vxlan
        |- nornir-hosts.yml          <- add your inventory for evpn-vxlan setup here if not yet defined
        |- tests
            |- 1.0                   <- arbitrary test name, you can use any other name recognized as dir
               |- test-commands.txt  <- list of commands to execute on the inventory devices
    ```

5. Execute `run --help` to see all available CLI options.
6. To proceed with the test run following command: `run -i <your-inventory> -t <test-name>`. For example, `run -i evpn-vxlan -t 1.0` will execute 1.0 test on the devices listed in the evpn-vxlan inventory. This will collect all the configs and commands listed in the test file at the time of the test execution. Keep into account, that the time may not be precise. For a better precision you can include some commands to collect time on a DUT.
7. By default outputs will contain a time stamp as part of directory names. To skip that, you can use `--no_timestamp` flag.
8. To collect `show tech support` if required, execute following command `run -i <your-inventory> -t tech` (with or without `--no_timestamp` flag). This will collect `show tech` on all devices and make some post-processing to remove unprintable characters (happens on EOS). **WARNING**: do not collect `show tech` often without a need. Git is not optimized to store big files. If you need that often, consider adding directory with show tech's to `.gitignore`.
9. You can also restore the configs previously collected with `--recover` option: `run -i <your-inventory> -r <full-path-to-the-dir-with-configs>`. By default this will execute in dry run mode without making any changes. To make the change, add `--no_dry_run` (short `-ndr`) flag.
