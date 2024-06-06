## Disk Prep
Start the Proxmox installer, but then go to a different virtual terminal to run commands.

### 1. Remove LVM Stuff:
If there are any other LVM things on the disk(s), the Proxmox installer fails. Here are some relevant commands to remove the LVM stuff.
```
lvs
lvremove
vgs
vgremove
pvs
pvremove
```
### 2. Clear Partition Tables
**After** LVM stuff has been wiped, clear partition tables. Repeat this command for each disk.
```
sgdisk /dev/sdx --zap-all
```
Hold the power button to reboot. The computer should boot to the USB drive because the SSD is no longer available.

⚠️ The 8.2-1 installer hangs at `3% create LVs` even after running the above commands. After about 4 minutes, it jumps to around 50% and then completes at a normal speed.

## General Configuration
*Once LVM and partitions are gone*, we can move on to the install.

Some basic details about the node need to be manually entered, including:
- (temporary) Password
- IP Address
- Gateway and DNS
- Domain
- Installation SSD Formatting

The PW is set to `easypass` initially, then changed by Ansible.



## Virtual Machines
These will be used in conjunction with PCIe Passthrough.

Create a VM with the Web GUI, then check the config with
```
qm config 103
```

The arguments to `qm create` are nearly 1:1 with the config output.
```
qm create 420 \
--agent 1 \
--bios ovmf \
--boot order='scsi0;ide2' \
--ciupgrade 0 \
--ciuser root \
--cores 16 \
--cpu host \
--efidisk0 local-lvm:0,efitype=4m \
--ide0 local-lvm:cloudinit,media=cdrom \
--ide2 local:iso/archlinux-2024.06.01-x86_64.iso,media=cdrom \
--ipconfig0 ip=192.168.0.4/24,gw=192.168.0.1 \
--machine q35 \
--memory 16384 \
--name workstationcli \
--net0 virtio,bridge=vmbr0 \
--numa 0 \
--ostype l26 \
--scsi0 iothread=1,local-lvm:32 \
--scsihw virtio-scsi-single \
--sshkeys ~/.ssh/authorized_keys \
--sockets 1
```

Iteratively generate the create command with a create/check/purge workflow
```sh
qm config 420
# check diff between 103 and 420
qm stop 420 -overrule-shutdown 1
qm destroy 420 --purge
```

## Arch Linux Install Notes
```
root@workstationcli ~ # fdisk -l
Disk /dev/sda: 32 GiB, 34359738368 bytes, 67108864 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

https://wiki.archlinux.org/title/Partitioning#UEFI/GPT_layout_example


https://github.com/jothi-prasath/archlinux-playbook/blob/master/tasks/swap.yml
- name: Update fstab to persist swap file
  become: true
  lineinfile:
    dest: /etc/fstab
    line: "{{ swapfile_path }} none swap defaults 0 0"
    state: present
  when: not swapfile_stat.stat.exists



possibly just use a cloud image
https://wiki.archlinux.org/title/Arch_Linux_on_a_VPS
https://gitlab.archlinux.org/archlinux/arch-boxes
https://geo.mirror.pkgbuild.com/images/latest/



The arguments to `qm create` are nearly 1:1 with the config output.
```
qm create 421 \
--agent 1 \
--bios ovmf \
--boot order=scsi0 \
--cores 16 \
--cpu host \
--efidisk0 local-lvm:0,efitype=4m \
--ide0 local-lvm:cloudinit,media=cdrom \
--ipconfig0 ip=192.168.0.4/24,gw=192.168.0.1 \
--machine q35 \
--memory 16384 \
--name cloudws \
--net0 virtio,bridge=vmbr0 \
--numa 0 \
--ostype l26 \
--scsi0 local-lvm:0,import-from=/root/Arch-Linux-x86_64-cloudimg.qcow2 \
--scsihw virtio-scsi-single \
--sshkeys ~/.ssh/authorized_keys \
--sockets 1
```

qm disk import 421 ~/Arch-Linux-x86_64-basic.qcow2 local-lvm
qm disk resize 421 scsi0 60G


[arch@cloudws ~]$ sudo fdisk -l
Disk /dev/sda: 2 GiB, 2147483648 bytes, 4194304 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: CACC5503-DD2D-41E4-B604-F0921D67E80B

Device      Start     End Sectors  Size Type
/dev/sda1    2048    4095    2048    1M BIOS boot
/dev/sda2    4096  618495  614400  300M EFI System
/dev/sda3  618496 4192255 3573760  1.7G Linux root (x86-64)


https://wiki.archlinux.org/title/Installation_guide



ln -sf /usr/share/zoneinfo/Europe/London /etc/localtime
hwclock --systohc



https://wiki.archlinux.org/title/Pacman
https://docs.ansible.com/ansible/latest/collections/community/general/pacman_module.html

-sysupgrade
-refresh


