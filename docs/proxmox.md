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


-- sshkeys ssh-rsa%20AAAAB3NzaC1yc2EAAAADAQABAAABgQCdu%2FDolq85%2FsScWhdmnFNpxYuCQtq6lPCuD%2FCcXbwy9TC372z7ZF2dvsWx0uHZFnTbbcuwvNmrR%2Fg2yROAmzoppEGvio8fIuv%2FiQ7V1lmplrBR1TWenr58S0PtHZ6NleGBuI3j6HSskoNwx3hRq9WyCvHdtWZ769tMRSOgG7YJJLyp4w0fX4cSeWwcSOhHhgVojI6%2FkqMIsEmeX691XDYT3vFLlY8Lsd%2FQzr6qe08o1xyzENOjUIT84fO%2FIKjvxQ6msIkcR%2FNrgELLz3M8GgMtdLU5w8%2ByTvM%2FxOEyaHxodpOloVkMBI4U%2FO4QXkyvO1GpyQq1YiQ%2Byg4O1Ul086wonxqj%2BBF%2BiktAmH9Vh%2BSjCiYRaOZn8GwUPkJ1zTz7xogtX7GOcnanYH2DXIIFfb8hVKdGrLdwZknyuHLie2rUctBYvmZ48yR1O6GrIclHj22WnYsji%2BLZqZ87IwBODTvfLSfIDcWFKb0l1IJzJNKcoErETWQekVnYC9lZeRhMdBs%3D%20ansible%0A \