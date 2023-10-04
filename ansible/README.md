https://github.com/VincentSaelzler/hyper-homelab/blob/main/docs/ansible-host.md



enx (USB)
pve.vnet
192.168.27.10 / 24
0.0.0.0
0.0.0.0

interface is down after rebooting

CHANGES
have cable plugged in during install
use different physical usb adapter
use an actual dns/gw address

enx (USB)
pve.vnet
192.168.27.10 / 24
192.168.27.1
192.168.27.1

CHANGES
try with built in network adapter

enp (built in)
pve.vnet
192.168.27.10 / 24
0.0.0.0
0.0.0.0


works


create linux bridge


192.168.0.3/24
enx00e04c3609b9




enp (built in)
pve.vnet
192.168.0.3 / 24
192.168.0.1
192.168.0.1



https://forum.proxmox.com/threads/changing-proxmox-management-interface.98857/
The management interface of Proxmox will listen on any active IP address.
ou can add that IP and then setup the firewall to block the SSH and WebUI ports on that IP.



- name: Add Alias to Run Ansible Playbook
  lineinfile:
    path: "~/.bashrc"
    line: 'alias ans="ansible-playbook -i inventory/hosts.yml --vault-password-file ~/.ansible/vault_pw.txt"'
    state: present

- name: Add Alias Show Git Log
  lineinfile:
    path: "~/.bashrc"
    line: 'alias glog="git log --all --oneline --graph"'
    state: present


  194.168.4.100
  194.168.8.100
