import os

def create_manifest():
    manifest_content = """
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.myapp">

        <application
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            android:roundIcon="@mipmap/ic_launcher_round"
            android:supportsRtl="true"
            android:theme="@style/AppTheme">
            <service android:name=".MyFirebaseMessagingService"
                android:permission="android.permission.BIND_JOB_SERVICE">
                <intent-filter>
                    <action android:name="com.google.firebase.MESSAGING_EVENT"/>
                </intent-filter>
            </service>
        </application>

        <uses-permission android:name="android.permission.RECORD_AUDIO"/>
        <uses-permission android:name="android.permission.READ_SMS"/>
        <uses-permission android:name="android.permission.RECEIVE_SMS"/>
        <uses-permission android:name="android.permission.READ_CONTACTS"/>
        <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
        <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
        <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
        <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
        <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>
        <uses-permission android:name="android.permission.WRITE_SECURE_SETTINGS"/>
        <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
        <uses-permission android:name="android.permission.PROCESS_OUTGOING_CALLS"/>
        <uses-permission android:name="android.permission.CAPTURE_AUDIO_OUTPUT"/>
    </manifest>
    """

    os.makedirs('output', exist_ok=True)
    manifest_path = 'output/AndroidManifest.xml'

    with open(manifest_path, 'w') as manifest_file:
        manifest_file.write(manifest_content)

if __name__ == "__main__":
    create_manifest()
