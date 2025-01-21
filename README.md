## Development Environment

Using a Windows environment. Linux requirements should be nearly identical.
* Docker (for Windows)
* VSCode
* Dev Containers Extension
* Git
* Azure CLI

## Quick Start

```sh
sudo apt install ansible
git clone https://github.com/VincentSaelzler/onebox/
ansible-playbook ansible/1_ansible-host.yml --ask-vault-pass --ask-become-pass
```

Dev Containers:

* Open Folder in Container (builds container)

**CRITICAL:** Then run the visual studio code command "Developer: Restart Pty Host"

* apples git settings
* applies bashrc aliases

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

### Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

1. OTHER Raspberry Pi OS
1. Lite 64 Bit
1. hostname: model4b.local
1. un/pw marcus/easypass
1. set time zone and keyboard layout
1. enable ssh with public key (from ansible vault / lastpass)

### Proxmox Virtualization Host

Wipe NVMe SSDs

```sh
# the adata one looks messed up.
# it shows different results after the same command is run multiple times
hexdump -C -n 1048576 /dev/nvme0n1 | tail

# first run
000ffe00  c6 dd d7 e2 a0 97 4b 88  19 a7 c2 89 72 75 85 d5  |......K.....ru..|
000ffe10  2e 58 10 ad 1d a0 e4 1b  c7 e3 8b 0c e6 23 6e 69  |.X...........#ni|
000ffe20  23 38 d5 33 d2 91 13 9a  21 58 61 75 41 7e 29 24  |#8.3....!XauA~)$|
[non-zero data continues all the way to....]
00100000

# second run
000ffe00  dd e0 66 66 02 00 00 c2  55 55 02 56 03 00 80 c1  |..ff....UU.V....|
000ffe10  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00100000

# perhaps (long shot) since the drive was formatted, but no data yet written,
# it returns arbitrary stuff until data is written?
badblocks -wsv /dev/nvme0n1
```

### Networking

Manually create the vlan bridge, or copy the interfaces file.

```sh
scp ./ansible/files/interfaces root@pve.local:/etc/network/interfaces
```

#### PCIe Passthrough

https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md

#### BIOS Configuration

* Update BIOS (from v1804 to v3205 to v3607)
* Reset All to Defaults
* Q-Fan Auto-Optimize
* Use 3200 MHz RAM Profile

## DNS API Credentials

Use porkbun.
