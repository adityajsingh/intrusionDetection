# this following python script would be used to send message to the targerted/ registered device
# this would likely be triggered when the machine finds any kind of wild animal


# importing the twilio library
from twilio.rest import Client

# SID of the twilio account
twilio_sid = 'YOUR DETAILS' 

# token id of twilio
twilio_secret = 'YOUR DETAILS' 

#my_number represents the number from which the message is to be sent
my_number = "YOUR DETAILS"

#other_number is the targerted number which will recieve the message
other_number = "YOUR DETAILS"

#creating the instance of the client
client = Client(twilio_sid, twilio_secret)


# the message that would be sent

def send_message(body):
    message_twilio = client.messages.create(
    body=body,
    from_=my_number,
    to=other_number
)

send_message("Hello")