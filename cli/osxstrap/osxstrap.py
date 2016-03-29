# -*- coding: utf-8 -*-

"""osxstrap.osxstrap: provides entry point main()."""


__version__ = "0.0.21"


import os

import click

import shutil

import common

import output

import ansible

import base64

from shutil import copyfile

install_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

config_path = os.path.join(os.path.expanduser("~"), '.config', 'osxstrap')

config_filename = 'main.osxstrap'


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--playbook', '-p', default='all', help='Playbook to run.')
@click.option('--ask-sudo-pass', '-k', default=False, is_flag=True, help='Have Ansible prompt you for a sudo password.')
@click.option('--ask-vault-pass', '-v', default=False, is_flag=True, help='Have Ansible prompt you for a vault password.')
def cli(ctx, playbook, ask_sudo_pass, ask_vault_pass):
	common.get_dotenv()
	if ctx.invoked_subcommand is None:	
		ansible.playbook(install_path, playbook, ask_sudo_pass, ask_vault_pass)


@cli.command()
def update():
	common.run('git pull origin master')
	ansible.galaxy_install(install_path)


@cli.command()
@click.option('-c', '--config-file', default=False, required=True, help='Path of downloaded config file to copy into place.')
def init(config_file):
	copy_config(config_file)
	ansible.galaxy_install(install_path)
	ansible.playbook(install_path, 'all', True, False)


def copy_config(source_path):
	source_path = os.path.join(os.getcwd(), source_path)
	destination_path = os.path.join(config_path, config_filename)
	if not source_path == False:
		if os.path.exists(source_path):
			if not os.path.exists(destination_path):
				common.mkdir(config_path)
				copyfile(source_path, destination_path)
			else:
				output.warning("Destination file %s already exists." % destination_path)
				if click.confirm('Do you want to overwrite it?'):
					os.remove(destination_path)
					copyfile(source_path, destination_path)
				else:
					output.abort("To run osxstrap without copying config, use the osxstrap command.")
		else:
			output.abort("Input file %s does not exist." % source_path)


@cli.command()
@click.option('-e', '--editor', default='webapp', required=False, help='Name of the program to use to edit osxstrap config (i.e. vim). Defaults to opening in the osxstrap webapp.')
def edit(editor):
	if editor == 'webapp':
		config_file_path = os.path.join(config_path, config_filename)
		if os.path.exists(config_file_path):
			f = open(config_file_path)
			config_string = f.read()
			f.close()
			encoded_config_string = base64.b64encode(config_string)
			print encoded_config_string
			common.run('open https://osxstrap.github.io#%s' % encoded_config_string)
		else:
			output.abort("%s does not exist." % config_file_path)
	else:
		common.run('%s %s' % (editor, os.path.join(config_path, config_filename)))