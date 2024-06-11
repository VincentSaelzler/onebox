
## Create Script to Check IOMMU Groups

Create a script file called `getgroups.sh`. Make it executable. Credit: [ArchWiki](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF#Ensuring_that_the_groups_are_valid)

```sh
#!/bin/bash
shopt -s nullglob
for d in /sys/kernel/iommu_groups/*/devices/*; do
    n=${d#*/iommu_groups/*}; n=${n%%/*}
    printf 'IOMMU Group %s ' "$n"
    lspci -nns "${d##*/}"
done | sort -V
```

## Proxmox KVM

[Proxmox Documentation](https://192.168.0.3:8006/pve-docs/pve-admin-guide.html#_emulated_devices_and_paravirtualized_devices)
The Q35 chipset provides a virtual PCIe bus
A SCSI controller of type VirtIO SCSI single and enabling the IO Thread setting is recommended. This is the default.

## Resources

- [No-GPU Proxmox Server Access over SERIAL](https://www.youtube.com/watch?v=ycue2GGh_dk)
- [Kernel Module Cheat Sheet](https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view)
- [PCI/GPU Passthrough on Proxmox VE 8 : Installation and configuration](https://forum.proxmox.com/threads/pci-gpu-passthrough-on-proxmox-ve-8-installation-and-configuration.130218/)
- [Working Config with NVIDIA RX 2060](https://github.com/VincentSaelzler/hyper-homelab/blob/main/docs/pcie-passthrough.md)
