# PCIe Passthrough

## BIOS

Setting|Note
-|-
Resize BAR|TODO Overlap w/other options?
IOMMU = Enable (Advanced > AMD CBS)|
SVM Mode = Enable (Advanced > CPU Configuration)|
Launch CSM = Disable (Advanced > Boot > CSM)|

## Proxmox Installation

Do via serial installer.

## GRUB

```sh
cat /proc/cmdline
# BOOT_IMAGE=/boot/vmlinuz-6.8.4-2-pve root=/dev/mapper/pve-root ro console=ttyS0,115200 quiet
```

### */etc/default/grub*

```sh
GRUB_CMDLINE_LINUX_DEFAULT="iommu=pt"

# things to consider...
GRUB_CMDLINE_LINUX_DEFAULT="initcall_blacklist=sysfb_init"
GRUB_TERMINAL=console
GRUB_TERMINAL=serial.
```

```sh
update-grub
reboot
cat /proc/cmdline
# BOOT_IMAGE=/boot/vmlinuz-6.8.4-3-pve root=/dev/mapper/pve-root ro console=ttyS0,115200 iommu=pt
```

## Kernel Modules

### */etc/modules*

```txt
vfio
vfio_iommu_type1
vfio_pci
```

```sh
lsmod | grep -i vfio
# [no output]
update-initramfs -u -k all
reboot
lsmod | grep -i vfio
# vfio_pci               16384  0
# vfio_pci_core          86016  1 vfio_pci
# irqbypass              12288  2 vfio_pci_core,kvm
# vfio_iommu_type1       49152  0
# vfio                   69632  3 vfio_pci_core,vfio_iommu_type1,vfio_pci
# iommufd                98304  1 vfio
```

```sh
lspci -nn
# 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)
lspci -s 09:00 -nnk
# 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)
#         Subsystem: Sapphire Technology Limited Sapphire Radeon RX 6700 [1da2:e445]
#         Kernel driver in use: amdgpu
#         Kernel modules: amdgpu
```

```sh
# /etc/modprobe.d/gpu-passthrough.conf   
blacklist amdgpu
options vfio-pci ids=1002:73df
```

```sh
lspci -s 09:00 -nnk
# 09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev df)
#         Subsystem: Sapphire Technology Limited Sapphire Radeon RX 6700 [1da2:e445]
#         Kernel driver in use: vfio-pci
#         Kernel modules: amdgpu
```

```sh
lspci -s 09:00 -nn
dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
dmesg | grep -i vfio
dmesg | grep 'remapping'
lspci -nnk | grep -B 2 -A 1 vfio
sysctl -a | grep video # not 1:1 naming with passed parameters
```
