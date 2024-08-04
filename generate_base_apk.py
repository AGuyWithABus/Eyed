import os

def generate_base_apk():
    os.makedirs('output', exist_ok=True)
    os.system("cp -r base_apk/* output/")
    print("Base APK generated in 'output/' directory.")

if __name__ == "__main__":
    generate_base_apk()
