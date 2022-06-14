# python script testing twilio API

from twilio.rest import Client

client = Client(
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)

for msg in client.messages.list():
    print(f"Deleting {msg.body}");
