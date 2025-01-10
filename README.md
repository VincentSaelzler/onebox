## Development Environment
Using a Windows environment. Linux requirements should be nearly identical.
- Docker (for Windows)
- VSCode
- Dev Containers Extension
- Git
- Azure CLI

## Quick Start
```sh
sudo apt install ansible
git clone https://github.com/VincentSaelzler/onebox/
ansible-playbook ansible/1_ansible-host.yml --ask-vault-pass --ask-become-pass
```
Dev Containers:
- Open Folder in Container (builds container)

**CRITICAL:** Then run the visual studio code command "Developer: Restart Pty Host"
  - apples git settings
  - applies bashrc aliases

```sh
# connect to Azure Data Lake Storage
# should work on noble 2024-05-21
# https://github.com/Azure/azure-cli/issues/28872
az login

# run playbooks
cd ansible
ans [playbook.yml]
```
### Useful Commands
```sh
# view git log in graph format
glog

# wipe out a container
pct destroy 103 --force true --destroy-unreferenced-disks true --purge true
```



## On-Premises Configuration

### Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

1. OTHER Raspberry Pi OS
1. Lite 64 Bit
1. hostname: model4b.local
1. un/pw marcus/easypass
1. set time zone and keyboard layout
1. enable ssh with public key (from ansible vault / lastpass)

Quidam Plebeius
Marcus Aurelius


### Proxmox Virtualization Host
#### PCIe Passthrough
https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md

#### BIOS Configuration
- Update BIOS (from v1804 to v3205 to v3607)
- Reset All to Defaults
- Q-Fan Auto-Optimize
- Use 3200 MHz RAM Profile





## DNS API Credentials
Use porkbun.