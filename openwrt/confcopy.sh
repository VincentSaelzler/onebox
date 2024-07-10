#!/bin/bash

# Check for the incoming parameters
if [ "$1" == "pull_default" ]; then
    LOCAL_PATH="default"
    REMOTE_HOST="192.168.1.1"
    DIRECTION="pull"
elif [ "$1" == "pull_current" ]; then
    LOCAL_PATH="old"
    REMOTE_HOST="192.168.27.1"
    DIRECTION="pull"
elif [ "$1" == "pull_new" ]; then
    LOCAL_PATH="new"
    REMOTE_HOST="192.168.27.1"
    DIRECTION="pull"
elif [ "$1" == "push_new" ]; then
    LOCAL_PATH="new"
    REMOTE_HOST="192.168.27.1"
    DIRECTION="push"
elif [ "$1" == "bootstrap" ]; then
    LOCAL_PATH="new"
    REMOTE_HOST="192.168.1.1"
    DIRECTION="push"
elif [ "$1" == "update" ]; then
    LOCAL_PATH="new"
    REMOTE_HOST="192.168.27.1"
    DIRECTION="push"
else
    echo "Invalid first parameter."
    exit 1
fi

# Variables
REMOTE_USER="root"
REMOTE_PATH="/etc/config"

# Files to copy
FILES=("firewall" "network" "wireless")

# Loop through each file and copy it based on the direction
for FILE in "${FILES[@]}"; do
    if [ "$DIRECTION" == "pull" ]; then
        scp -O "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/${FILE}" "${LOCAL_PATH}/${FILE}"
        if [ $? -eq 0 ]; then
            echo "Successfully copied ${FILE} to ${LOCAL_PATH}"
        else
            echo "Failed to copy ${FILE}"
        fi
    elif [ "$DIRECTION" == "push" ]; then
        scp -O "${LOCAL_PATH}/${FILE}" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/${FILE}"
        if [ $? -eq 0 ]; then
            echo "Successfully copied ${FILE} to ${REMOTE_HOST}:${REMOTE_PATH}"
        else
            echo "Failed to copy ${FILE}"
        fi
    fi
done
