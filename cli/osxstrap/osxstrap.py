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

main_config_path = os.path.join(os.path.expanduser("~"), '.config', 'osxstrap', 'config.osxstrap')

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
@click.option('--config-file-path', '-c', default=False, help='Path of downloaded config file to copy into place.')
def init(config_file_path):
	copy_config(config_file_path)
	update()
	ansible.playbook(install_path, 'all', True, False)


def copy_config(source_path):
	if not source_path == False:
		if os.path.exists(source_path):
			copyfile(source_path, main_config_path)
		else:
			return False
