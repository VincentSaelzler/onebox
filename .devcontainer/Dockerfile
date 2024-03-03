FROM ubuntu:latest

RUN apt update
RUN apt full-upgrade -y
RUN apt install -y git python3-pip

# to fix bug "Ansible could not initialize the preferred locale: unsupported locale"
# https://github.com/ansible/vscode-ansible/issues/690#issuecomment-1645185319
RUN apt install -y language-pack-en

# RUN python3 -m pip install --user ansible
RUN python3 -m pip install ansible

# upload files to blob storage via azure cli
RUN apt-get install -y curl
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
