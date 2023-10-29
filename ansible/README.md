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