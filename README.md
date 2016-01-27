# osxstrap

osxstrap provides an easier way to provision your OSX El Capitan workstation using Ansible. It aims to be different than other similar projects in its focus on consolidated portable configuration, reusable Ansible roles, and zero dependency setup.

## Quick Start

1. Clone the configuration repo (https://github.com/osxstrap/osxstrap-config) and modify `config.yml` to your liking.

2. Run the installer script, passing in the URL of your cloned configuration repo:

	curl -s https://raw.githubusercontent.com/osxstrap/osxstrap/master/osxstrap | bash -s -- -g https://github.com/{YOUR_USERNAME}/osxstrap-config.git

## Install Script

### Options

```
-h      Show help message.

-v      Enable verbose output.

-p      Name of a playbook inside of 'osxstrap/playbooks'
        (file name without the .yml extension) to be run.
        i.e. osxstrap -p osx-computername

-t      Run playbook with tags.

-g      URL of a git repo to clone containing 
        configuration files. Will bypass interactive
        osxstrap config generation. See 
        https://github.com/osxstrap/osxstrap-config
        for an example. (optional)

-c      URL of a configuration file to download.
        Will bypass interactive osxstrap config
        generation. (optional)

-k      Force the ansible-playbook command to prompt
        for a sudo password. Overrides the
        osxstrap['prompt_sudo'] var.

-u      Update osxstrap using git and roles using
        ansible-galaxy.

-i      Install directory path.
        Default: ~/.osxstrap

-r      Git repo URL to install osxstrap from. 
         Default: https://github.com/osxstrap/osxstrap

-d      Install in development mode.

-l      Development mode only: path in which to search
        for git repos of roles, to symlink to the
        roles directory.

-s      Skip role install.

-x      Force interactive creation of config/osxstrap.yml,
        even if it already exists.
```

## What's Included

## Development

-d      Install in development mode.
   -l      Development mode only: path in which to search for git repos of roles, to symlink to the roles directory.
   -p      Name of a playbook inside of 'osxstrap/playbooks' (file name without the .yml extension) to be run. i.e. osxstrap -p osx-computername
   -t      Run playbook with tags.
   
## Issues

Please report any issues to this repositories issue tracker https://github.com/osxstrap/osxstrap/issues.

## Credits

Created by [Jeremy Litten](https://github.com/jeremyltn).

Inspired by

https://github.com/superlumic

https://github.com/spencergibb/ansible-osx

https://github.com/debops

and many others.

See individual repositories at https://github.com/osxstrap for Ansible role credits.