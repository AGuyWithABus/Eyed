import subprocess
import os
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

    # Compile Java files
    javac_cmd = [
        'javac',
        '-source', '1.8',
        '-target', '1.8',
        '-d', build_dir,
        '-cp', android_jar,
        f'{src_dir}/*.java'
    ]

    print(f"Running javac command: {' '.join(javac_cmd)}")
    subprocess.run(javac_cmd, check=True)

    # Convert .class files to .dex format
    d8_cmd = [
        'd8',
        '--output', 'build',
        build_dir
    ]

    print(f"Running d8 command: {' '.join(d8_cmd)}")
    subprocess.run(d8_cmd, check=True)

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
    subprocess.run(aapt_cmd, check=True)

    # Add classes.dex to the APK
    with open(unsigned_apk_file, 'ab') as apk:
        with open(dex_output_file, 'rb') as dex:
            shutil.copyfileobj(dex, apk)

    # Sign the APK (this step is optional, depending on your use case)
    # sign_cmd = [
    #     'apksigner', 'sign',
    #     '--ks', 'my-release-key.jks',
    #     '--out', final_apk_file,
    #     unsigned_apk_file
    # ]
    # print(f"Running apksigner command: {' '.join(sign_cmd)}")
    # subprocess.run(sign_cmd, check=True)

    # For now, just copy the unsigned APK as the final APK
    shutil.copy(unsigned_apk_file, final_apk_file)
    print(f"APK compiled successfully at: {final_apk_file}")

if __name__ == "__main__":
    try:
        compile_apk()
    except subprocess.CalledProcessError as e:
        print(f"Error running {e.cmd}: {e}")
        print("Failed at compile_apk.py. Stopping the process.")
