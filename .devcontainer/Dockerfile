# base image
FROM ubuntu
# apt dependencies
RUN apt update && apt full-upgrade -y
RUN apt install -y git ansible
# fixes
# ERROR: Ansible could not initialize the preferred locale: unsupported locale setting  
RUN apt install -y locales
RUN locale-gen --purge en_US.UTF-8
