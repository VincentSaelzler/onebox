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
- Update BIOS (from v1804 to v3205)
- Reset All to Defaults
- Q-Fan Auto-Optimize
- Use 3200 MHz RAM Profile

#### Enable IOMMU and Virtualization. Disable Legacy Boot.
- IOMMU = Enable (Advanced > AMD CBS)
- SVM Mode = Enable (Advanced > CPU Configuration)
- Launch CSM = Disable (Advanced > Boot > CSM)

#### craft computing's instructions:
https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view
- machine type matches host type
- non-balooning


## DNS API Credentials
I don't have a static IP with my ISP, and want to keep things as simple as possible.

A container is configured to directly update GoDaddy DNS records in case my public IP changes, instead of using an external dynamic DNS service.

Manually log in to GoDaddy and [Create Keys](https://developer.godaddy.com/keys). 
- name: ansible
- environment: production

Save in vault as `vault_godaddy_key_and_secret` in the format `key:secret`
