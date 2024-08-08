import firebase_admin
from firebase_admin import credentials, messaging
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Path to your service account key file
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_message(topic, message_body):
    try:
        message = messaging.Message(
            data={
                'message': message_body
            },
            topic=topic,
        )
        response = messaging.send(message)
        logging.info('Successfully sent message: %s', response)
    except Exception as e:
        logging.error('Failed to send message: %s', e)

def main():
    logging.info("Server is running. Enter 'exit' to stop.")
    while True:
        command = input("Enter the command to send to the device: ")
        if command.lower() == 'exit':
            break
        send_message('device_topic', command)

if __name__ == "__main__":
    main()
