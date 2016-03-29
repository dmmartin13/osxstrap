# -*- coding: utf-8 -*-

"""osxstrap.ansible: Ansible management for osxstrap."""

import os

import output

import common

def galaxy_install(install_path):
	roles_path = os.path.join(install_path, 'roles')
	common.mkdir(roles_path)
	common.run('ansible-galaxy install -f -r "%s" -p "%s"' % (os.path.join(install_path, 'requirements.yml'), roles_path))

def playbook(install_path, playbook='all', ask_sudo_pass=False, ask_vault_pass=False, extras=None):
	common.get_dotenv()
	os.environ["ANSIBLE_CONFIG"] = os.path.join(install_path, 'ansible.cfg')
	command_string = 'ansible-playbook'
	command_string += ' -i "%s"' % os.path.join(install_path, 'inventory')
	if ask_sudo_pass or os.environ.get("OSXSTRAP_ASK_SUDO_PASS") == '1':
		command_string += ' --ask-sudo-pass'
	if ask_vault_pass or os.environ.get("OSXSTRAP_ASK_VAULT_PASS") == '1':
		command_string += ' --ask-vault-pass'
	if extras:
		command_string += ' ' + extras
	command_string += ' "' + os.path.join(install_path, 'playbooks', playbook) + '.yml"'
	common.run(command_string)