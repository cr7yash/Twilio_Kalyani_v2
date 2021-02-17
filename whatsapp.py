import datetime
import emoji
import os
import schedule
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = client = Client()

global from_whatsapp_number
from_whatsapp_number = 'whatsapp:+14155238886'
global to_whastapp_number
to_whastapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

def create_message():
	now = datetime.datetime.now()
	message = ""
	if now.hour>8 and now.hour<9:
		message = "Don't give up Kalyani...You have come too far for that.\n"
		message += "1. Learn from your mistakes\n"
		message += "2. Don't repeat your mistakes\n\n"
		message += "Remember that time back in 2014 when you learned how to write "
		message += "code for the first time? Remember that feeling?"
		message += "How would the 17 year old Kalyani react if she learns how fragile you've become?"
		message += "It'll all be fine. It'll all be great. Don't you worry. Believe in yourself!"
	elif now.hour>17 and now.hour<18:
		message = 'Stretch, lift weights, drink water, bathe, eat, relax. '
	elif now.hour>22:
		message = 'Go to sleep now. You can work again in the morning. No harm will be done. Less time will be wasted.'

	return message

def send_message():
	message = create_message()
	# print(message)
	client.messages.create(
		body=message, 
		from_=from_whatsapp_number,
		to=to_whastapp_number)

def main():
	schedule.every(5).minutes.do(send_message)
	while True:
		schedule.run_pending()

if __name__ == '__main__':
	main()
