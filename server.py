import firebase_admin
from firebase_admin import credentials, messaging

def initialize_firebase():
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def send_command(command):
    message = messaging.Message(
        data={
            "command": command,
        },
        topic="all",
    )
    response = messaging.send(message)
    print(f'Successfully sent command: {response}')

if __name__ == "__main__":
    initialize_firebase()
    while True:
        command = input("Enter command: ")
        send_command(command)
