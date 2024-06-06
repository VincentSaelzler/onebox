## Resources
- [No-GPU Proxmox Server Access over SERIAL](https://www.youtube.com/watch?v=ycue2GGh_dk)
- [Kernel Module Cheat Sheet](https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view)
[PCI/GPU Passthrough on Proxmox VE 8 : Installation and configuration](https://forum.proxmox.com/threads/pci-gpu-passthrough-on-proxmox-ve-8-installation-and-configuration.130218/)
[Working Config with NVIDIA RX 2060](https://github.com/VincentSaelzler/hyper-homelab/blob/main/docs/pcie-passthrough.md)

#### Enable IOMMU and Virtualization. Disable Legacy Boot.
- IOMMU = Enable (Advanced > AMD CBS)
- SVM Mode = Enable (Advanced > CPU Configuration)
- Launch CSM = Disable (Advanced > Boot > CSM)



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


- machine bios matches host type
- non-balooning

## Proxmox KVM
[Proxmox Documentation](https://192.168.0.3:8006/pve-docs/pve-admin-guide.html#_emulated_devices_and_paravirtualized_devices)
A VM’s Machine Type defines the hardware layout of the VM’s virtual motherboard. You can choose between the default Intel 440FX or the Q35 chipset, which also provides a virtual PCIe bus, and thus may be desired if you want to pass through PCIe hardware. Additionally, you can select a vIOMMU implementation.

A SCSI controller of type VirtIO SCSI single and enabling the IO Thread setting for the attached disks is recommended if you aim for performance. This is the default for newly created Linux VMs since Proxmox VE 7.3.

pre-enroll-keys specifies if the efidisk should come pre-loaded with distribution-specific and Microsoft Standard Secure Boot keys. It also enables Secure Boot by default (though it can still be disabled in the OVMF menu within the VM).


[Arch SSH Install](https://wiki.archlinux.org/title/Install_Arch_Linux_via_SSH)
Using an additional FAT formatted drive
Using an additional ISO