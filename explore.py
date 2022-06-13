# python script testing twilio API

from twilio.rest import Client

client = Client(
    "ACe7ecba6048ff3b33d7f068d9f99f112e",
    "1173ed6f4ced8c73d3f232060529582a"
)

for msg in client.messages.list():
    print(f"Deleting {msg.body}");