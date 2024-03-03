# Windows Host
Docker for Windows

VSCode

Dev Containers Extension

# Ansible Container
Bootstrap
```sh
cd ansible
ansible-playbook 1.0-ansible-host.yml --inventory ./inventory/hosts.yml --ask-vault-pass
# login to azure
az login
# quit shell session and start a new one (to apply .bashrc)
cd ansible
ans [other playbooks]
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