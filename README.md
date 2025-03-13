## Bootstrapping

See `Bootstrapping.md`


Check the websites repo and set up ruby gems.

## Proxmox Virtualization Host

```sh
scp ~/onebox/ansible/files/interfaces root@pve.saelzler.org:/etc/network/interfaces
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

## SSH Certificate Based

```sh
mkdir ~/ca
ssh-keygen -t ed25519 -f ~/ca/host -C host_ca
ssh-keygen -t ed25519 -f ~/ca/client -C client_ca
sudo ssh-keygen -h -s ~/ca/host -I palatine.saelzler.org -n palatine.saelzler.org /etc/ssh/ssh_host_ed25519_key.pub
# sudo nano /etc/ssh/sshd_config
HostCertificate /etc/ssh/ssh_host_ed25519_key-cert.pub
TrustedUserCAKeys /etc/ssh/client_ca.pub
Subsystem sftp /usr/lib/openssh/sftp-server
######################################################
sudo systemctl restart sshd

echo -n '@cert-authority *.saelzler.org ' > ~/ca/known_host && cat ~/ca/host.pub >> ~/ca/known_host
# copy/paste over content in C:\Users\vince\.ssh\known_hosts
scp C:\Users\vince\.ssh\id_ed25519.pub palatine.saelzler.org:~/ca/blue.pub # from blue

ssh-keygen -s ~/ca/client -I vince@blue.saelzler.org -n vince ~/ca/blue.pub
sudo cp ~/ca/client.pub /etc/ssh/client_ca.pub
```
