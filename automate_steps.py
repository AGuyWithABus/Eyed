import subprocess

def run_command(command):
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)

def extract_apk():
    print("Extracting APK...")
    run_command("apktool d base.apk -o extracted_apk")

def modify_apk():
    # Placeholder for modifying APK files, if needed
    print("Modifying APK... (Placeholder)")

def rebuild_apk():
    print("Rebuilding APK...")
    run_command("apktool b extracted_apk -o modified_base.apk")

def sign_apk():
    # Replace with your actual keystore file path
    print("Signing APK...")
    run_command("apksigner sign --ks my-release-key.jks --out my-signed-app.apk modified_base.apk")

def install_apk():
    print("Installing APK...")
    run_command("adb install my-signed-app.apk")

def main():
    extract_apk()
    modify_apk()
    rebuild_apk()
    sign_apk()
    install_apk()

if __name__ == "__main__":
    main()
