# Bootstrapping

## Modem / Router (Quantum Fiber C5500XK)

https://192.168.0.1

Utilities > Restore Defaults > Restore Modem to Factory Default State

## Ryzen (Proxmox)

```sh
minicom --device /dev/ttyUSB0
```

⚠️ power off proxmox box  
⚠️ insert installer flash drive  
⚠️ power on proxmox box  

Boot inturrupts:

* F2 = BIOS
* F8 = Boot Options

### Wipe SSDs

Used BIOS secure erase on Crucial NVMe. **Choose 4K block size.**

Notes:

* Crucial drive seems to work perfectly, and gives option between 4K and 512 block sizes.
* ADATA drive technically does seem to erase. However, it is confisuing because it loads the drive with random data which changes from read-to-read until someting is written. so it is hard to tell whether stuff is actually erased.

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

## Ansible Controller (Surface and/or Desktop VM)

```sh
echo "samplepass" > ~/.ansible_vault_password # 🚨🚨🚨
chmod 600 ~/.ansible_vault_password
sudo pacman -S python-pipx
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

```sh
ssh-copy-id root@192.168.0.27

```
