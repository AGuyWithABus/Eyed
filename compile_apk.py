import subprocess
import os
import shutil

def decompile_apk(base_apk, output_dir):
    print(f"Decompiling {base_apk}...")
    subprocess.run(['apktool', 'd', '-f', base_apk, '-o', output_dir], check=True)
    print(f"Decompiled {base_apk} to {output_dir}")

def inject_code(src_dir, target_dir):
    print(f"Injecting code from {src_dir} to {target_dir}...")
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(src_dir, target_dir)
    print("Code injection completed.")

def recompile_apk(output_dir, output_apk):
    print(f"Recompiling APK from {output_dir}...")
    subprocess.run(['apktool', 'b', output_dir, '-o', output_apk], check=True)
    print(f"Recompiled APK saved as {output_apk}")

def main():
    base_apk = "base.apk"  # Path to your prebuilt base APK
    output_dir = "decompiled_apk"
    src_dir = "output/src/com/example/myapp"  # Generated Java code directory
    target_dir = os.path.join(output_dir, 'smali/com/example/myapp')
    output_apk = "modified.apk"  # Path for the final APK

    try:
        # Step 1: Decompile the base APK
        decompile_apk(base_apk, output_dir)
        
        # Step 2: Inject the generated code
        inject_code(src_dir, target_dir)
        
        # Step 3: Recompile the APK
        recompile_apk(output_dir, output_apk)
        
        print("APK modification process completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during APK processing: {e}")
        print("Failed at compile_apk.py. Stopping the process.")

if __name__ == "__main__":
    main()
