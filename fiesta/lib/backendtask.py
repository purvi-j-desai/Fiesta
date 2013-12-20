from celery.task import Task
from celery.loaders import load_settings
import facebook

class mytask(Task):
    def run(self, my_parameter, **kwargs):
        assert my_parameter, "Missing Args"
        print("parameter received here in controller: %s" %my_parameter)
        oauth_access_token = my_parameter
        print("access token is : %s" %oauth_access_token)
    	graph = facebook.GraphAPI(oauth_access_token)
    	user = graph.get_object("me")
    	print "User JSON:"
    	print user
        family = graph.get_connections(user["id"], "family")
        print "Family JSON:"
        print family
        print "Extra stuff.."
        print (family["data"][0]["id"])
	myrelative = graph.get_object(family["data"][0]["id"])
	print myrelative["first_name"]
	print "My relative JSON:"
        print myrelative

#Need to store this collected data in database
