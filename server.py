import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account key file
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_message(topic, message_body):
    message = messaging.Message(
        data={
            'message': message_body
        },
        topic=topic,
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)

def main():
    while True:
        command = input("Enter the command to send to the device: ")
        send_message('device_topic', command)

if __name__ == "__main__":
    main()
 
