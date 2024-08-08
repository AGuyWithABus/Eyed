#!/bin/bash

# Update package lists and upgrade existing packages
apt update && apt upgrade -y

# Install necessary packages
apt install -y python clang git zip unzip wget rust

# Upgrade pip to the latest version
pip install --upgrade pip

# Install Python dependencies
pip install firebase-admin

# Install APKTool
echo "Installing APKTool..."

# Create a bin directory in your home directory
mkdir -p ~/bin

# Download the APKTool jar and script
wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O ~/bin/apktool
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.8.1.jar -O ~/bin/apktool.jar

# Make the APKTool script executable
chmod +x ~/bin/apktool

# Add the bin directory to your PATH in the current session
export PATH=$PATH:$HOME/bin

# Optionally, permanently add the bin directory to your PATH
echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

# Check APKTool version to verify installation
apktool --version
