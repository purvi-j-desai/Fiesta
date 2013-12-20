from celery.task import Task
from celery.loaders import load_settings
import facebook
from mongoengine import *
import documents

class posttask(Task):
    def run(self, my_parameter, **kwargs):
	print "In posttask!!!"
	try:
		print "notifying"
		fb_response = graph.put_wall_post('Hello from celebrations!!', \
                profile_id = my_parameter)
    		print "Done posting :D %s" %fb_response
	except facebook.GraphAPIError as e:
    		print 'Something went wrong:', e.type, e.message
                
