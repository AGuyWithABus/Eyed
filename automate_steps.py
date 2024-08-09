import subprocess
import os
import shutil

def run_command(command):
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)

def extract_apk():
    # Remove existing directory if it exists
    if os.path.exists("extracted_apk"):
        shutil.rmtree("extracted_apk")
    run_command("apktool d base.apk -o extracted_apk")

def rebuild_apk():
    run_command("apktool b extracted_apk -o modified_base.apk")

def main():
    extract_apk()
    rebuild_apk()

if __name__ == "__main__":
    main()
