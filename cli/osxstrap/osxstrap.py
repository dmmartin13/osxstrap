# -*- coding: utf-8 -*-

"""osxstrap.osxstrap: provides entry point main()."""


__version__ = "0.0.21"


import os

import click

import shutil

import common

import output

import ansible

from shutil import copyfile

install_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

config_path = os.path.join(os.path.expanduser("~"), '.config', 'osxstrap')

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--playbook', '-p', default='all', help='Playbook to run.')
@click.option('--ask-sudo-pass', '-k', default=True, is_flag=True, help='Have Ansible prompt you for a sudo password.')
@click.option('--ask-vault-pass', '-v', default=False, is_flag=True, help='Have Ansible prompt you for a vault password.')
def cli(ctx, playbook, ask_sudo_pass, ask_vault_pass):
    if ctx.invoked_subcommand is None:
    	ansible.playbook(install_path, playbook, ask_sudo_pass, ask_vault_pass)


@cli.command()
def update():
	common.run('git pull origin master')
	ansible.galaxy_install(install_path)


@cli.command()
@click.option('-c', default=False, required=True, help='Path of downloaded config file to copy into place.')
def init(c):
	copy_config(c)
	ansible.galaxy_install(install_path)
	ansible.playbook(install_path, 'all', True, False)


def copy_config(source_path):
	destination_path = os.path.join(config_path, os.path.basename(source_path))
	if not source_path == False:
		if os.path.exists(source_path):
			if not os.path.exists(destination_path):
				common.mkdir(config_path)
				copyfile(source_path, destination_path)
			else:
				output.error("%s already exists, not copying input file %s." % (destination_path, source_path))
		else:
			output.error("Input file %s does not exist." % source_path)
