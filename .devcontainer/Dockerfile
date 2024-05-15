# base image
FROM ubuntu
RUN apt update && apt full-upgrade -y

# fixes ERROR: Ansible could not initialize the preferred locale: unsupported locale setting  
RUN apt install -y locales
RUN locale-gen --purge en_US.UTF-8

# project dependencies
RUN apt install -y git ansible sshpass python3-proxmoxer