import subprocess
import os
import glob
import shutil

def compile_apk():
    # Define paths
    src_dir = 'output/src/com/example/myapp'
    build_dir = 'build/intermediates/classes/debug'
    android_jar = os.path.expandvars("$ANDROID_SDK/platforms/android-29/android.jar")
    apk_output_dir = 'output/apk'
    dex_output_file = 'build/classes.dex'
    unsigned_apk_file = 'build/unsigned.apk'
    final_apk_file = os.path.join(apk_output_dir, 'MyApp.apk')

    # Create necessary directories
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(apk_output_dir, exist_ok=True)

    # Get all Java files
    java_files = glob.glob(os.path.join(src_dir, "*.java"))
    
    if not java_files:
        print(f"No Java files found in {src_dir}. Aborting.")
        return

    # Compile Java files
    javac_cmd = [
        'javac',
        '-source', '1.8',
        '-target', '1.8',
        '-d', build_dir,
        '-cp', android_jar
    ] + java_files  # add all Java files to the command

    print(f"Running javac command: {' '.join(javac_cmd)}")
    try:
        subprocess.run(javac_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running javac: {e}")
        print("Javac command output:")
        print(e.output)  # Print the output to get more information
        print("Failed at compile_apk.py. Stopping the process.")
        return

    # Convert .class files to .dex format
    d8_cmd = [
        'd8',
        '--output', 'build',
        build_dir
    ]

    print(f"Running d8 command: {' '.join(d8_cmd)}")
    try:
        subprocess.run(d8_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running d8: {e}")
        print("Failed at compile_apk.py. Stopping the process.")
        return

    # Create the APK structure
    os.makedirs('build/apk', exist_ok=True)
    shutil.copy(dex_output_file, 'build/apk/classes.dex')

    # Use aapt to package the APK
    aapt_cmd = [
        'aapt', 'package',
        '-f',
        '-m',
        '-M', 'output/src/main/AndroidManifest.xml',
        '-S', 'output/src/main/res',
        '-I', android_jar,
        '-F', unsigned_apk_file,
        '-A', 'output/src/main/assets'
    ]

    print(f"Running aapt command: {' '.join(aapt_cmd)}")
    try:
        subprocess.run(aapt_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running aapt: {e}")
        print("Failed at compile_apk.py. Stopping the process.")
        return

    # Add classes.dex to the APK
    with open(unsigned_apk_file, 'ab') as apk:
        with open(dex_output_file, 'rb') as dex:
            shutil.copyfileobj(dex, apk)

    # For now, just copy the unsigned APK as the final APK
    shutil.copy(unsigned_apk_file, final_apk_file)
    print(f"APK compiled successfully at: {final_apk_file}")

if __name__ == "__main__":
    try:
        compile_apk()
    except subprocess.CalledProcessError as e:
        print(f"Error running {e.cmd}: {e}")
        print("Failed at compile_apk.py. Stopping the process.")
