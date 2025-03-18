# Bootstrapping

*Install software on physical devices. Once this is all done, we are ready to use Ansible to automate the rest of the setup.*

## Microsoft Surface

Run powershell as **administrator**

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent
ssh-add -D
ssh-add -l

ssh-keygen -t ed25519 
# use throw-away PW. it is saved "securely" by Windows so won't be needed again. 🚨🚨🚨 MS account
ssh-add $env:USERPROFILE\.ssh\id_ed25519
rm $env:USERPROFILE\.ssh\id_ed25519
rm $env:USERPROFILE\.ssh\known_hosts
rm $env:USERPROFILE\.ssh\known_hosts.old
dir $env:USERPROFILE\.ssh
ssh-add -l
cat $env:USERPROFILE\.ssh\id_ed25519.pub
```

## Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

```
Raspberry Pi OS (64-bit)
palatine
marcus
🚨🚨🚨 [from lastpass]
Europe/London
gb
Enable SSH > Allow public-key authentication only > Paste public key
```

start raspberry pi plugged into monitor and mouse/keyboard

turn on serial port and then enable login console over serial port (gui radio buttons)

```sh
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_serial_cons 0
```

connect to serial via "Serial Monitor" vscode extension. All defaults except us terminal mode

```sh
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub | cut --delimiter=' ' --fields=2
```

ssh from surface

```sh
ssh marcus@palatine
# 🚨🚨🚨 compare the fingerprints
```

unplug pi from mouse/keyboard

```sh
sudo apt update
sudo apt full-upgrade -y
sudo apt autoremove -y
sudo reboot
```

```sh
ssh marcus@palatine
```

```sh
echo "samplepass" > ~/.ansible_vault_password # 🚨🚨🚨
chmod 600 ~/.ansible_vault_password
rpi-connect on
rpi-connect signin # 🚨🚨🚨 Raspberry Pi ID (backed by google account)
sudo apt install pipx -y
pipx install ansible-core
pipx ensurepath
source ~/.bashrc
ansible-galaxy collection install community.general
git clone https://github.com/VincentSaelzler/onebox/
cp ~/onebox/ansible/files/controller/ansible.cfg ~/.ansible.cfg
ansible-playbook ~/onebox/ansible/0-ansible-controller.yml
source ~/.bashrc
ssh-keygen -t ed25519 # 🚨🚨🚨 [passphrase from lastpass]
eval `ssh-agent`
ssh-add ~/.ssh/id_ed25519
```

## Ryzen

```sh
ssh marcus@palatine
minicom --device /dev/ttyUSB0
```

⚠️ power off proxmox box  
⚠️ ethernet to lan port on router  
⚠️ display cable to monitor  
⚠️ monitor input to display port  
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

```txt
Install Proxmox VE (Terminal UI, Serial Console)

Target harddisk: /dev/[CAN VARY] (CT1000P3PSSD8) (931.51 GiB)
root pw:  🚨🚨🚨 from lastpass

 ┌──────────────────────┤ Proxmox VE (8.3-1) Installer ├──────────────────────┐
 │                                                                            │
 │   Option                            ┆ Selected value                       │
 │ ├────────────────────────────────────────────────────────────────────────┤ │
 │   Bootdisk filesystem               ┆ ext4                                 │
 │   Bootdisk(s)                       ┆ /dev/nvme1n1                         │
 │   Timezone                          ┆ Europe/London                        │
 │   Keyboard layout                   ┆ United Kingdom                       │
 │   Administrator email               ┆ root@pve.saelzler.org                │
 │   Management interface              ┆ enp7s0                               │
 │   Hostname                          ┆ pve.saelzler.org                     │
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
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub | cut --delimiter=' ' --fields=2
```
