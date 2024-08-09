#!/bin/bash

# Update and install required packages
pkg update -y
pkg upgrade -y

# Install APKTool
pkg install -y apktool

# Install OpenJDK for apksigner
pkg install -y openjdk-17

# Install adb
pkg install -y android-tools

echo "Tools installed successfully."
