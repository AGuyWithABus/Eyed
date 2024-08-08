#!/data/data/com.termux/files/usr/bin/bash

# Update and install necessary packages
pkg update && pkg upgrade
pkg install -y python wget openjdk-17

# Install firebase-admin using pip
echo "Installing firebase-admin..."
pip install firebase-admin

# Install apktool
echo "Installing apktool..."

# Define versions
APKTOOL_VERSION="2.8.0"
APKTOOL_JAR="apktool_${APKTOOL_VERSION}.jar"
APKTOOL_URL="https://github.com/iBotPeaches/Apktool/releases/download/${APKTOOL_VERSION}/apktool_${APKTOOL_VERSION}.jar"
APKTOOL_BIN="apktool"

# Download apktool jar
wget "$APKTOOL_URL" -O "$APKTOOL_JAR"

# Create apktool script
echo '#!/data/data/com.termux/files/usr/bin/bash' > "$APKTOOL_BIN"
echo "java -jar $(pwd)/$APKTOOL_JAR \"\$@\"" >> "$APKTOOL_BIN"

# Make the script executable
chmod +x "$APKTOOL_BIN"

# Move script to /data/data/com.termux/files/usr/bin/ for easy access
mv "$APKTOOL_BIN" /data/data/com.termux/files/usr/bin/

# Verify installations
echo "Verifying installations..."
echo "Firebase-admin version:"
pip show firebase-admin
echo "Apktool version:"
apktool --version
