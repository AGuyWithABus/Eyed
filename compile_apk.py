import subprocess
import os

def compile_apk():
    commands = [
        "cd output",
        "mkdir -p build/intermediates/classes/debug",
        "javac -source 1.8 -target 1.8 -d build/intermediates/classes/debug -cp $ANDROID_SDK/platforms/android-29/android.jar src/com/example/myapp/*.java",
        "mkdir -p build/intermediates/res/merged/debug",
        "cp -r res/* build/intermediates/res/merged/debug/",
        "mkdir -p build/outputs/apk/debug",
        "aapt package -f -m -J src -M AndroidManifest.xml -S build/intermediates/res/merged/debug -I $ANDROID_SDK/platforms/android-29/android.jar",
        "dx --dex --output=build/intermediates/classes/debug/classes.dex build/intermediates/classes/debug",
        "aapt package -f -m -F build/outputs/apk/debug/app.unaligned.apk -M AndroidManifest.xml -S build/intermediates/res/merged/debug -I $ANDROID_SDK/platforms/android-29/android.jar",
        "aapt add build/outputs/apk/debug/app.unaligned.apk build/intermediates/classes/debug/classes.dex",
        "zipalign -v 4 build/outputs/apk/debug/app.unaligned.apk build/outputs/apk/debug/app.apk",
        "apksigner sign --ks my-release-key.jks --out build/outputs/apk/debug/app-signed.apk build/outputs/apk/debug/app.apk"
    ]

    for command in commands:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        if process.returncode != 0:
            print(f"Error executing command: {command}")
            print(process.stderr)
            return
        print(process.stdout)

if __name__ == "__main__":
    compile_apk()
