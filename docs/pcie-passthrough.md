# PCIe Passthrough

## BIOS

Section|Setting|Note
-|-|-
Advanced > PCI Subsystem Settings > Above 4G Decoding|Enabled|Result of top right "Resize BAR" option = ON
Advanced > PCI Subsystem Settings > Resize BAR Support|Auto|Result of top right "Resize BAR" option = ON
Advanced > AMD CBS > IOMMU|Enabled
Boot > CSM > Launch CSM|Disabled|Force UEFI boot
Boot > Booth Configuration > POST Delay Time|10 sec
AI Tweaker > AI Overclock Tuner|D.O.C.P.|RAM Overclock

## Proxmox Installation

Serial Connection to Windows

- Connect USB to Serial CH340 Adapter
- Open device manager to get COM number
- Open in PuTTY with speed **9600**
- Close PuTTY and reopen with speed **115200**

Use the **serial installer**.

## GRUB

```sh
# before
cat /proc/cmdline
> BOOT_IMAGE=/boot/vmlinuz-6.8.4-2-pve root=/dev/mapper/pve-root ro console=ttyS0,115200 quiet

# etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="iommu=pt"
# ---

update-grub
reboot

# after
cat /proc/cmdline
> BOOT_IMAGE=/boot/vmlinuz-6.8.4-3-pve root=/dev/mapper/pve-root ro console=ttyS0,115200 iommu=pt
```

## Kernel Modules

```sh
# before
lsmod | grep -i vfio
> [no output]

# /etc/modules
vfio
vfio_iommu_type1
vfio_pci
# ---

# update-initramfs -u -k all (not required?)
reboot

# after
lsmod | grep -i vfio
> vfio_pci               16384  0
> vfio_pci_core          86016  1 vfio_pci
> irqbypass              12288  2 vfio_pci_core,kvm
> vfio_iommu_type1       49152  0
> vfio                   69632  3 vfio_pci_core,vfio_iommu_type1,vfio_pci
> iommufd                98304  1 vfio
```

## Modprobe Options

```sh
# locate gpu device
lspci -nn
> 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)

# before
lspci -s 09:00 -nnk
> 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)
>         Subsystem: Sapphire Technology Limited Sapphire Radeon RX 6700 [1da2:e445]
>         Kernel driver in use: amdgpu
>         Kernel modules: amdgpu

# /etc/modprobe.d/gpu-passthrough.conf   
blacklist amdgpu
options vfio-pci ids=1002:73df
# ---

reboot

# after
lspci -s 09:00 -nnk
> 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)
>         Subsystem: Sapphire Technology Limited Sapphire Radeon RX 6700 [1da2:e445]
>         Kernel driver in use: vfio-pci
>         Kernel modules: amdgpu
```

## Related Commands

```sh
lspci -s 09:00 -nn
dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
dmesg | grep -i vfio
dmesg | grep 'remapping'
lspci -nnk | grep -B 2 -A 1 vfio
sysctl -a | grep video # not 1:1 naming with passed parameters
```

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

- The Q35 chipset provides a virtual PCIe bus
- A SCSI controller of type VirtIO SCSI single and enabling the IO Thread setting is recommended. This is the default.

## Resources

- [No-GPU Proxmox Server Access over SERIAL](https://www.youtube.com/watch?v=ycue2GGh_dk)
- [Kernel Module Cheat Sheet](https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view)
- [PCI/GPU Passthrough on Proxmox VE 8 : Installation and configuration](https://forum.proxmox.com/threads/pci-gpu-passthrough-on-proxmox-ve-8-installation-and-configuration.130218/)
- [Working Config with NVIDIA RX 2060](https://github.com/VincentSaelzler/hyper-homelab/blob/main/docs/pcie-passthrough.md)
