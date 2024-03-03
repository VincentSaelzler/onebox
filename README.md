# Windows Host
Manually install:
- Docker for Windows
- VSCode
- Dev Containers Extension

# Clone Repo
"Cloine in a unique volume" option seems broken. Error when trying to reach github.com.

Clone to Windows first, then reopen in container.

# Ansible Container
Bootstrap
```sh
# on your mark
apt install git python3-pip
python3 -m pip install ansible

# get ready
cd ansible
apt install language-pack-en # fixes runtime bug in vs code dev containers
ansible-playbook ansible-host.yml -i inventory/hosts.yml --ask-vault-pass

# get set
source ~/.bashrc
az login

# go
ans [playbook.yml]
```


# BIOS Configuration
- Update BIOS (from v1804 to v3205)
- Reset All to Defaults
- Q-Fan Auto-Optimize
- Use 3200 MHz RAM Profile

# Install Proxmox



# PCIe Passthrough
https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md

## Configure Motherboard BIOS
Enable IOMMU and Virtualization. Disable Legacy Boot.
- IOMMU = Enable (Advanced > AMD CBS)
- SVM Mode = Enable (Advanced > CPU Configuration)
- Launch CSM = Disable (Advanced > Boot > CSM)

craft computing's instructions:
https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view



# machine type matches host type
# non-balooning