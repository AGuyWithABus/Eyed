#!/bin/bash

# Update package lists and upgrade existing packages
apt update && apt upgrade -y

# Install necessary packages
apt install -y python clang git zip unzip wget

# Install Rust (needed for some Python packages)
pkg install rust -y

# Upgrade pip to the latest version
pip install --upgrade pip

# Install Python dependencies
pip install firebase-admin

# APKTool installation instructions (requires manual setup)
echo "Installing APKTool..."

# Fetching the APKTool jar and wrapper script
wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.8.1.jar -O /usr/local/bin/apktool.jar

# Make the APKTool script executable
chmod +x /usr/local/bin/apktool

# Check APKTool version
apktool --version
