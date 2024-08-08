#!/bin/bash

cd /home/bart/homeassistant/config

# Activate the virtual environment
source /home/bart/homeassistant/bin/activate

# Run the Home Assistant script
# hass --script check_config

# Stage all changes for commit
# git add .
git add mycode
git add configuration.yaml

# Show the current status of staged changes
git status

# Prompt the user for a commit message
read -p "Enter the Description for the Change: " CHANGE_MSG

# Commit the staged changes with the entered message
git commit -m "${CHANGE_MSG}"

# Push the changes to the remote repository
git push origin master

exit