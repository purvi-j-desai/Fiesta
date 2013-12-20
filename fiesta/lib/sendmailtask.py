from celery.task import Task
from celery.loaders import load_settings
import facebook
import smtplib
from mongoengine import *
import documents

class mailtask(Task):
    def run(self, email_id, name, message, **kwargs):
	try:
        	assert email_id, "Missing Args"
	except AssertionError:
		print "Assertion Error"
	else:
        	receiver_id = email_id
		receiver_name = name
		msg = """From: leesafrank <leesafrank90@gmail.com>
                To: To Person < """ + receiver_id + """ >
		Subject:  ***Notification***

		Hi """ + receiver_name + """,""" + message
		
		sender = 'leesafrank90@gmail.com'
		try:
			smtpObj = smtplib.SMTP('smtp.gmail.com', 25)
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login('leesafrank90@gmail.com','leesafrank123')	
			smtpObj.sendmail(sender, receiver_id, msg)         
			smtpObj.quit()
   			print "Successfully sent email"
		except:
			print "Sending Error"	
