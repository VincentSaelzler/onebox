## Development Environment
Using a Windows environment. Linux requirements should be nearly identical.
- Docker (for Windows)
- VSCode
- Dev Containers Extension
- Git
- Azure CLI

## Quick Start
```sh
git clone https://github.com/VincentSaelzler/onebox/
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