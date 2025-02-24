## Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

📒 Choose the one with a GUI to connect via Raspberry Pi Connect

1. Default / Recommended OS
1. hostname: backdoor.local
1. un/pw vince/[from lastpass]
1. set time zone and keyboard layout
1. enable ssh with public key only [key from lastpass]

Configure Raspberry Pi Connect: Run all commands in the [documentation](https://www.raspberrypi.com/documentation/services/connect.html)

Inject secret vault password and set up aliases to use that plus the inventory file.

```sh
ssh vince@backdoor
```

```sh
sudo apt update
sudo apt full-upgrade
sudo apt autoremove
sudo reboot
```

```sh
ssh vince@backdoor
```

```sh
sudo apt install ansible git
git clone https://github.com/VincentSaelzler/onebox/
cd onebox/ansible
ansible-playbook 0-ansible-bootstrap.yml --ask-vault-pass
source ~/.bashrc
glog # ...to confirm the aliases are applied
```

Complete the ansible controller setup now that we have full access to inventory variables and vault secrets.

```sh
cd ~/onebox/ansible
ans 0-ansible-controller.yml
```

Check the websites repo and set up ruby gems.

## Proxmox Virtualization Host

```sh
ssh vince@backdoor
minicom --device /dev/ttyUSB0
```

⚠️ power off proxmox box  
⚠️ ethernet to lan port on router  
⚠️ display cable to monitor  
⚠️ insert installer flash drive  
⚠️ keyboard to proxmox box  
⚠️ power on proxmox box  

Boot inturrupts:

* F2 = BIOS
* F8 = Boot Options

### Wipe SSDs

Used BIOS secure erase on Crucial NVMe. **Choose 4K block size.**

Notes:

* Crucial drive seems to work perfectly, and gives option between 4K and 512 block sizes.
* ADATA drive technically does seem to erase. However, it is confisuing because it loads the drive with random data which changes from read-to-read until someting is written. so it is hard to tell whether stuff is actually erased.

⚠️ keyboard to windows as proxmox box reboots  

```
Install Proxmox VE (Terminal UI, Serial Console)
```

```txt
Target harddisk: /dev/[CAN VARY] (CT1000P3PSSD8) (931.51 GiB)
root pw:  (only temporary - ansible will change it)
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
 │   Host IP (CIDR)                    ┆ 192.168.27.159/24                    │
 │   Gateway                           ┆ 192.168.27.1                         │
 │   DNS                               ┆ 192.168.27.1                         │
 │                                                                            │
 │                                                                            │
 │           [X] Automatically reboot after successful installation           │
 │                                                                            │
 │  <Abort>                                             <Previous> <Install>  │
 └────────────────────────────────────────────────────────────────────────────┘
```

```sh
scp ~/onebox/ansible/files/interfaces root@pve:/etc/network/interfaces
```

⚠️ power off proxmox box  
⚠️ ethernet to tagged port on router  
⚠️ power on proxmox box  

```sh
cd ~/onebox/ansible
ans 1_full-setup.yml
```

see `7_frigate.yml` on how to change frigate web ui password

## Reolink Cameras

Initializate via Reolink App (NOT Web UI)

### Palace

⚠️ Plug both power and ethernet into doorbell  
⚠️ Hold physical reset button around 7 seconds (loud noise will happen)

Setting|Value
-|-
Add Device > IP/Domain | palacecam-wired.local
Camera Name | Palace
Wi-Fi | Enter SSID and PW
Display > OSD | Hide Name + Watermark
Light > Status LED | Stay Off
Network Advanced > Server Settings > HTTPS | On
Stream > Clear > Resolution | 1920x2560 (default)
Stream > Clear > FPS | 15
Stream > Clear > Max Bitrate | 6144 (max allowed option)
Stream > Clear > I-frame Interval | 1x
Stream > Frame Rate Mode | Constant

### Living Room

⚠️ Hold physical reset button around 15 seconds.  
⚠️ No indication of reset happening, but was available within 60 sec

Setting|Value
-|-
Add Device > IP/Domain | livingroomcam.local
Camera Name | Living Room
Display > OSD | Date/Time in Top Left
Stream > Clear > Resolution | 2560x1920 (default)
Stream > Clear > FPS | 15
Stream > Clear > Max Bitrate | 8192 (max allowed option)
Stream > Clear > I-frame Interval | 1x
Stream > Frame Rate Mode | Constant
Stream > Bitrate Mode | Constant Bitrate

### Both

Setting|Value
-|-
Network > Advanced > NTP Settings > NTP Server | openwrt.local
System > Date & Time > Set Up > Time Zone | Dublin, Edinburgh, London
System > Date & Time > Set Up > DST | On
System > Date & Time > Set Up > DST > Start | Mar - Last - Sun - 01:00
System > Date & Time > Set Up > DST > End   | Oct - Last - Sun - 02:00
System > Date & Time > Date Format | YYYY/MM/DD

## PCIe Passthrough

<https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md>

## BIOS Configuration

* Update BIOS (from v1804 to v3205 to v3607)
* Reset All to Defaults
* Q-Fan Auto-Optimize
* Use 3200 MHz RAM Profile

## Containers

```sh
# wipe out a container
pct destroy 103 --force true --destroy-unreferenced-disks true --purge true
```
