# base image
FROM ubuntu
RUN apt update && apt full-upgrade -y

# fixes ERROR: Ansible could not initialize the preferred locale: unsupported locale setting  
RUN apt install -y locales
RUN locale-gen --purge en_US.UTF-8

# project dependencies
RUN apt install -y git vim ansible sshpass python3-proxmoxer

RUN  echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers
RUN apt install -y sudo
