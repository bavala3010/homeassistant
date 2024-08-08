#!/bin/bash

# Define the folder and file to retain
FOLDER="mycode"
FILE="configuration.yaml"

# Navigate to the root of the repository
cd /home/bart/homeassistant/config

# Filter the commit history
git filter-branch --prune-empty --tag-name-filter cat -- --all