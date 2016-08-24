#!/usr/bin/env python

from twilio.rest import TwilioRestClient

account_sid = "ACaf0162d9ba9e0c22ba551fb374e37fc0" # Your Account SID from www.twilio.com/console
auth_token  = "1423704d54124697900eda448d9cb1eb"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Nanodegree",
    to="+13038888769",    # Replace with your phone number
    from_="+19706338080") # Replace with your Twilio number

print(message.sid)
