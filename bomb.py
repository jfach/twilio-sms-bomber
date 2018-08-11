import os
import sys
import time
from twilio.rest import TwilioRestClient

aexport twilio_bomb_sid=TWILIO_ACCOUNT_SID
export twilio_bomb_token=TWILIO_AUTH_TOKEN
export twilio_bomb_number=TWILIO_NUMBER

client = TwilioRestClient(account_sid, auth_token)

recipient = sys.argv[1]
message = sys.argv[2]
if len(sys.argv) == 4:
	message_count = int(sys.argv[3])
else:
	message_count = 1

for x in range(0, message_count):
	message = client.messages.create(
		body=str(message),
		to=str(recipient),
		from_=str(from_number))
	print str(x + 1) + " message(s) sent!"
	print "Message SID: " + message.sid
	time.sleep(1)
