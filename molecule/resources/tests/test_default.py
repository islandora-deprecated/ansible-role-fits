import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_fits_install_dir_exists(host):
    assert host.file("/opt/fits-1.5.0").is_directory


def test_fits_executable(host):
    output = host.check_output("/opt/fits-1.5.0/fits.sh -h")

    assert (
        """usage: fits
 -f <arg>   alternate fits.xml configuration file location (optional)
 -h         print this message
 -i <arg>   input file or directory (required)
 -n         output directories are nested when recursively processing
            nested directories (when -r is set and -i is a directory)
            (optional)
 -o <arg>   Directs the FITS output to a file or directory (if -i is a
            directory) rather than console
 -r         process directories recursively when -i is a directory
 -v         print version information
 -x         convert FITS output to a standard metadata schema -- note:
            only standard schema metadata is output
 -xc        output using a standard metadata schema and include FITS xml"""
        in output
    )
