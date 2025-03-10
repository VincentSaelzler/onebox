# Bootstrapping

## Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

1. Default / Recommended OS with GUI
1. do NOT set username/password
1. hostname: backdoor
1. set time zone and keyboard layout
1. do NOT enable ssh

start raspberry pi connect from GUI

🚨🚨🚨 sign in with Raspberry Pi ID (Google Account 2 Factor?)

```sh
###################################
sudo apt update
sudo apt full-upgrade -y
sudo apt autoremove -y
sudo apt install pipx
pipx install ansible-core
pipx ensurepath
sudo reboot
###################################
ansible-galaxy collection install community.general
echo "samplepass" > ~/.ansible/vault_password # 🚨🚨🚨
chmod 600 ~/.ansible/vault_password
git clone https://github.com/VincentSaelzler/onebox/
cp ~/onebox/ansible/files/controller/ansible.cfg ~/.ansible.cfg
ansible-playbook ~/onebox/ansible/0-ansible-bootstrap.yml
source ~/.bashrc
apb ~/onebox/ansible/0-ansible-controller.yml
# TODO: Check the websites repo and set up ruby gems.
```
