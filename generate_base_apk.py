import os

def create_directory_structure(base_dir):
    dirs = [
        os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', 'app'),
        os.path.join(base_dir, 'src', 'main', 'res', 'layout'),
        os.path.join(base_dir, 'src', 'main', 'res', 'values'),
        os.path.join(base_dir, 'src', 'main', 'res', 'drawable'),
        os.path.join(base_dir, 'src', 'main', 'assets'),
        os.path.join(base_dir, 'src', 'main', 'libs'),
    ]
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)

def create_android_manifest(base_dir):
    manifest_content = """<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>"""
    manifest_path = os.path.join(base_dir, 'src', 'main', 'AndroidManifest.xml')
    with open(manifest_path, 'w') as manifest_file:
        manifest_file.write(manifest_content)

def create_basic_resources(base_dir):
    # strings.xml
    strings_content = """<resources>
    <string name="app_name">MyApp</string>
</resources>"""
    strings_path = os.path.join(base_dir, 'src', 'main', 'res', 'values', 'strings.xml')
    with open(strings_path, 'w') as strings_file:
        strings_file.write(strings_content)

    # activity_main.xml
    layout_content = """<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, World!" />

</LinearLayout>"""
    layout_path = os.path.join(base_dir, 'src', 'main', 'res', 'layout', 'activity_main.xml')
    with open(layout_path, 'w') as layout_file:
        layout_file.write(layout_content)

def create_basic_java_class(base_dir):
    java_content = """package com.example.app;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}"""
    java_path = os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', 'app', 'MainActivity.java')
    with open(java_path, 'w') as java_file:
        java_file.write(java_content)

def create_build_config(base_dir):
    build_gradle_content = """apply plugin: 'com.android.application'

android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.example.app"
        minSdkVersion 16
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'com.google.android.material:material:1.3.0'
}"""
    build_gradle_path = os.path.join(base_dir, 'build.gradle')
    with open(build_gradle_path, 'w') as build_gradle_file:
        build_gradle_file.write(build_gradle_content)

def generate_base_apk():
    base_dir = 'base_apk'
    create_directory_structure(base_dir)
    create_android_manifest(base_dir)
    create_basic_resources(base_dir)
    create_basic_java_class(base_dir)
    create_build_config(base_dir)
    print(f"Base APK structure generated in '{base_dir}' directory.")

if __name__ == "__main__":
    generate_base_apk()
