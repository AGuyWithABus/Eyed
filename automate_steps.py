import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_name):
    logging.info(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Error running {script_name}: {result.stderr}")
        return False
    logging.info(f"{script_name} output:\n{result.stdout}")
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
            logging.error(f"Failed at {script}. Stopping the process.")
            return

    logging.info("APK generation and compilation completed successfully.")

if __name__ == "__main__":
    main()
