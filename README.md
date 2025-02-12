## Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

1. OTHER Raspberry Pi OS
1. Lite 64 Bit
1. hostname: backdoor.local
1. un/pw vince/[from lastpass]
1. set time zone and keyboard layout
1. enable ssh with public key only [key from lastpass]

Inject secret vault password and set up aliases to use that plus the inventory file.

```sh
ssh vince@backdoor
sudo apt update
sudo apt full-upgrade
sudo apt autoremove
sudo reboot
ssh vince@backdoor
sudo apt install ansible git
git clone https://github.com/VincentSaelzler/onebox/
cd onebox/ansible
ansible-playbook 0-ansible-bootstrap.yml --ask-vault-pass
source ~/.bashrc
```

Complete the ansible controller setup now that we have full access to inventory variables and vault secrets.

```sh
glog # git log
ans 0-ansible-controller.yml
```





## Proxmox Virtualization Host

Boot inturrupts:

* F2 = BIOS
* F8 = Boot Options

### Wipe SSDs

Used BIOS secure erase on Crucial NVMe. **Choose 4K block size.**

Notes:

* Crucial drive seems to work perfectly, and gives option between 4K and 512 block sizes.
* ADATA drive technically does seem to erase. However, it is confisuing because it loads the drive with random data which changes from read-to-read until someting is written. so it is hard to tell whether stuff is actually erased.

### Install Proxmox via Serial

Start a serial terminal on the raspberry pi **before** turning on the computer.

```sh
sudo apt install minicom
minicom --device /dev/ttyUSB0
```

Plug the computer into a port on VLAN 27 **before** turning on the computer.

The keyboard can be unplugged from the proxmox computer and back to raspberry pi serial while it is booting. Proxmox sends a serial version of the boot menu. Run serial installer

```txt
Target harddisk: /dev/nvme1n1 (CT1000P3PSSD8) (931.51 GiB)
root pw: easypass (only temporary - ansible will change it)
email: admin@pve.local
networking: defaults should be correct, assuming static DHCP reservation is configured

 ┌──────────────────────┤ Proxmox VE (8.3-1) Installer ├──────────────────────┐
 │                                                                            │
 │   Option                            ┆ Selected value                       │
 │ ├────────────────────────────────────────────────────────────────────────┤ │
 │   Bootdisk filesystem               ┆ ext4                                 │
 │   Bootdisk(s)                       ┆ /dev/nvme1n1                         │
 │   Timezone                          ┆ Europe/London                        │
 │   Keyboard layout                   ┆ United Kingdom                       │
 │   Administrator email               ┆ admin@pve.local                      │
 │   Management interface              ┆ enp7s0                               │
 │   Hostname                          ┆ pve.local                            │
 │   Host IP (CIDR)                    ┆ 192.168.29.159/24                    │
 │   Gateway                           ┆ 192.168.29.1                         │
 │   DNS                               ┆ 192.168.29.1                         │
 │                                                                            │
 │                                                                            │
 │           [X] Automatically reboot after successful installation           │
 │                                                                            │
 │  <Abort>                                             <Previous> <Install>  │
 └────────────────────────────────────────────────────────────────────────────┘
```

### Networking

Manually create the vlan bridge, or copy the interfaces file.

```sh
scp ./ansible/files/interfaces root@pve.local:/etc/network/interfaces
```

Reboot or "apply configuration"

**Move to the tagged port**

### Reolink Camera

#### Initialization via Reolink App (NOT Web UI)

* Set PW
* Camera Name: Food

Display

* OSD > Hide Everything

Stream

* Clear
  + Max Bitrate (kbps): 8192 (max allowed option)
  + I-frame Interval: 1x
* Bitrate Mode: Constant Bitrate

Sounds

* Record Audio: On

Network

* Advanced > Server Settings
  + RTSP: On / 554


#### PCIe Passthrough

<https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md>

#### BIOS Configuration

* Update BIOS (from v1804 to v3205 to v3607)
* Reset All to Defaults
* Q-Fan Auto-Optimize
* Use 3200 MHz RAM Profile

## DNS API Credentials

Use porkbun.


## Containers

```sh
# wipe out a container
pct destroy 103 --force true --destroy-unreferenced-disks true --purge true
```