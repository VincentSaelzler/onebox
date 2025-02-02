# Get the Petcube Working from Chamonix

## Container

devenv

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCdu/Dolq85/sScWhdmnFNpxYuCQtq6lPCuD/CcXbwy9TC372z7ZF2dvsWx0uHZFnTbbcuwvNmrR/g2yROAmzoppEGvio8fIuv/iQ7V1lmplrBR1TWenr58S0PtHZ6NleGBuI3j6HSskoNwx3hRq9WyCvHdtWZ769tMRSOgG7YJJLyp4w0fX4cSeWwcSOhHhgVojI6/kqMIsEmeX691XDYT3vFLlY8Lsd/Qzr6qe08o1xyzENOjUIT84fO/IKjvxQ6msIkcR/NrgELLz3M8GgMtdLU5w8+yTvM/xOEyaHxodpOloVkMBI4U/O4QXkyvO1GpyQq1YiQ+yg4O1Ul086wonxqj+BF+iktAmH9Vh+SjCiYRaOZn8GwUPkJ1zTz7xogtX7GOcnanYH2DXIIFfb8hVKdGrLdwZknyuHLie2rUctBYvmZ48yR1O6GrIclHj22WnYsji+LZqZ87IwBODTvfLSfIDcWFKb0l1IJzJNKcoErETWQekVnYC9lZeRhMdBs= ansible

ansible-vault view inventory/group_vars/all/vault.yml --vault-password-file ~/.ansible/vault_pw.txt

vlan 27

## DHCP and Port Forward

104

bc:24:11:59:e0:02

27486

## Visual Studio Code

ansible-vault decrypt files/vault/id_rsa --vault-password-file ~/.ansible/vault_pw.txt

## Ansible

```txt
kennylong.kubernetes-yaml-formatter
davidanson.vscode-markdownlint (too opinionated)
```

<https://192.168.27.215:8971>

## GROUND-UP REBUILD

```sh
# delete frigate and revproxy containers
ans 4_containers.yml
ans 7_frigate.yml
# docker logs frigate | grep "***    Password:"
ans 11_proxy.yml
```
