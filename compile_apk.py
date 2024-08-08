import os
import subprocess

def compile_apk():
    os.makedirs('build', exist_ok=True)
    os.makedirs('build/intermediates/classes/debug', exist_ok=True)
    os.makedirs('build/intermediates/res/merged/debug', exist_ok=True)
    os.makedirs('build/outputs/apk/debug', exist_ok=True)

    # Compile Java files
    javac_cmd = [
        'javac', '-source', '1.8', '-target', '1.8',
        '-d', 'build/intermediates/classes/debug',
        '-cp', '$ANDROID_SDK/platforms/android-29/android.jar',
        'src/com/example/myapp/*.java'
    ]
    subprocess.run(javac_cmd, check=True)

    # Merge resources
    aapt_package_cmd = [
        'aapt', 'package', '-f', '-m', '-J', 'src',
        '-M', 'output/AndroidManifest.xml',
        '-S', 'output/res',
        '-I', '$ANDROID_SDK/platforms/android-29/android.jar'
    ]
    subprocess.run(aapt_package_cmd, check=True)

    # Create classes.dex
    dx_cmd = [
        'dx', '--dex', '--output=build/intermediates/classes/debug/classes.dex',
        'build/intermediates/classes/debug'
    ]
    subprocess.run(dx_cmd, check=True)

    # Package APK
    aapt_package_apk_cmd = [
        'aapt', 'package', '-f', '-m', '-F',
        'build/outputs/apk/debug/app.unaligned.apk',
        '-M', 'output/AndroidManifest.xml',
        '-S', 'output/res',
        '-I', '$ANDROID_SDK/platforms/android-29/android.jar'
    ]
    subprocess.run(aapt_package_apk_cmd, check=True)

    # Add classes.dex to APK
    aapt_add_cmd = [
        'aapt', 'add', 'build/outputs/apk/debug/app.unaligned.apk',
        'build/intermediates/classes/debug/classes.dex'
    ]
    subprocess.run(aapt_add_cmd, check=True)

    # Align APK
    zipalign_cmd = [
        'zipalign', '-v', '4',
        'build/outputs/apk/debug/app.unaligned.apk',
        'build/outputs/apk/debug/app.apk'
    ]
    subprocess.run(zipalign_cmd, check=True)

    # Sign APK
    apksigner_cmd = [
        'apksigner', 'sign', '--ks', 'my-release-key.jks',
        '--out', 'build/outputs/apk/debug/app-signed.apk',
        'build/outputs/apk/debug/app.apk'
    ]
    subprocess.run(apksigner_cmd, check=True)

if __name__ == "__main__":
    compile_apk()
