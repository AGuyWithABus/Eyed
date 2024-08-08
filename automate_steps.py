import os
import subprocess
import platform

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        return False
    print(result.stdout)
    return True

def install_tools():
    # Ensure the install_tools.sh script exists and is executable
    if not os.path.isfile('install_tools.sh'):
        print("Error: install_tools.sh not found.")
        return False

    # Make sure install_tools.sh is executable
    os.chmod('install_tools.sh', 0o755)

    # Run the install_tools.sh script
    result = subprocess.run(['./install_tools.sh'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error installing tools: {result.stderr}")
        return False
    print(result.stdout)
    return True

def main():
    # First install tools
    if not install_tools():
        print("Failed to install tools. Stopping the process.")
        return

    # Run other scripts
    scripts = [
        'generate_base_apk.py',
        'create_manifest.py',
        'implement_java_code.py',
        'compile_apk.py'
    ]

    for script in scripts:
        if not run_script(script):
            print(f"Failed at {script}. Stopping the process.")
            return

    print("APK generation and compilation completed successfully.")

if __name__ == "__main__":
    main()
