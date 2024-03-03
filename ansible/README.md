## Quick Start
```sh
ansible-playbook ./ansible/1.0-ansible-host.yml --inventory ./ansible/inventory/hosts.yml --ask-vault-pass
# open new bash terminal
cd ansible
ans [playbook].yml
```

## Ansible Vault
```sh
ansible-vault encrypt inventory/group_vars/all/vault.yml --vault-password-file ~/.ansible/vault_pw.txt
ansible-vault view inventory/group_vars/all/vault.yml --vault-password-file ~/.ansible/vault_pw.txt
ansible-vault edit inventory/group_vars/all/vault.yml --vault-password-file ~/.ansible/vault_pw.txt
```

## Ansible Debugging
Debug multiple variables at once:
```yml
  - debug:
      var: "{{ item }}"
    with_items:
      - hostvars.pve.lan_vbridge
      - hostvars.pve.lan_presence
      - hostvars.pve.lan_iface
```

## Dev Environment
Two noteworthy aliases are installed with the `aliases` role.
```sh
alias ans # run an ansible playbook
alias glog # git log with graph format
```


## GoDaddy DNS Configuration via API
I don't have a static IP with my ISP, and want to keep things as simple as possible.

A container is configured to directly update GoDaddy DNS records in case my public IP changes, instead of using an external dynamic DNS service.

Manually log in to GoDaddy and [Create Keys](https://developer.godaddy.com/keys). 
- name: ansible
- environment: production

Save in vault as `vault_godaddy_key_and_secret` in the format `key:secret`
