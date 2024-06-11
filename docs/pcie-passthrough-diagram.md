
## BIOS

###

Setting|Note
-|-
Resize BAR|TODO Overlap w/other options?
IOMMU = Enable (Advanced > AMD CBS)|
SVM Mode = Enable (Advanced > CPU Configuration)|
Launch CSM = Disable (Advanced > Boot > CSM)|

## GRUB

### /etc/default/grub

    GRUB_CMDLINE_LINUX_DEFAULT="quiet initcall_blacklist=sysfb_init"
    GRUB_TERMINAL=console

    GRUB_CMDLINE_LINUX console=ttyS0
    GRUB_TERMINAL=serial.

###

```sh
grub-mkconfig -o /boot/grub/grub.cfg
```

###

```sh
cat /proc/cmdline
[...] ro console=ttyS0,115200 quiet
```

## Kernel Modules

### /etc/modules

    vfio
    vfio_iommu_type1
    vfio_pci

###

```sh
update-initramfs -u -k all
lsmod | grep -i vfio
```

### /etc/modprobe.d/vfio.conf

    options vfio-pci ids=1a2b:3c4d
    options vfio-pci ids=1a2b:3c4d disable_vga=1

###

```sh
update-initramfs -u -k all
dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
lspci -nnk | grep -B 2 -A 1 vfio
sysctl -a | grep video # not 1:1 naming with passed parameters
```
