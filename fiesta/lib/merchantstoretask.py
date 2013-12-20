from celery.task import Task
from celery.loaders import load_settings
import facebook
from mongoengine import *
import documents
from sendmailtask import mailtask
from postonwalltask import posttask

class merchanttask(Task):
    def run(self, param1, param2, param3, param4, param5, **kwargs):
	try:
        	assert param1, "Missing Args"
	except AssertionError:
		print "Assertion Error"
	else:
		doc_id = param1 #doc id obtained
		fb_id = documents.Merchant.objects(id=doc_id).first().fb_id  #fb id obtained
		#store remaining details
		merchant = documents.Merchant.objects(id=doc_id)
		merchant.update_one(set__email = documents.User.objects(fb_uid=fb_id).first().email)
		for i in merchant:
			i.reload()
		merchant.update_one(set__name = documents.User.objects(fb_uid=fb_id).first().user_name)
		for i in merchant:
			i.reload()
		merchant.update_one(set__site_url = param2)
		for i in merchant:
			i.reload()
		merchant.update_one(set__dealer_in = param3)
		for i in merchant:
			i.reload()
		merchant.update_one(set__contact_no = param4)
		for i in merchant:
			i.reload()
		merchant.update_one(set__store_name = param5)
		for i in merchant:
			i.reload()
		print "done storing in task"
