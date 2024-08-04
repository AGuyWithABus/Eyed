import os
import subprocess

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        return False
    print(result.stdout)
    return True

def main():
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
