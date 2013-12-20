import logging
import facebook
import cgi
import urllib
import urllib2
from pylons import request, response, session, config, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import pymongo
import json
import documents
from backendtask import mytask
from fiesta.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UserauthController(BaseController):

    def __before__(self):
        self.appid = config['facebook.appid']
        self.secret = config['facebook.secret']
                
    def auth(self):
	try:
		config['storeid'] = request.params['storeid']
	except:
		print "Storeid not a param.."
        if (request.params['user'] == 'merchant'):
                config['user'] = 'merchant'
        	return render('/oauth_merchant_redirect.mako')
	if (request.params['user'] == 'customer'):
		config['user'] = 'customer'
        	return render('/oauth_user_redirect.mako')
	
 
    def authnext(self):
        params = request.params.copy()
	code = params.pop("code", None)
        #-----------code obtained successfully----------------
        redirect_url = 'http://'+config['myhost']+':5000/userauth/authnext'
        args = dict(client_id=self.appid, redirect_uri=redirect_url)
        args["client_secret"] = self.secret
        args["code"] = code 
        resp = cgi.parse_qs(urllib.urlopen(
        "https://graph.facebook.com/oauth/access_token?" +
        urllib.urlencode(args)).read())	
        if resp:
		oauth_access_token = resp["access_token"][-1] #access token fetched
		config['accesstoken'] = oauth_access_token 
                #getting user json
		print "Received Access token: %s" % oauth_access_token 	
 		graph = facebook.GraphAPI(oauth_access_token)
                user = graph.get_object("me")
                #dB storage
                existing_user = documents.User.objects(fb_uid = user['id']).first()
		if existing_user:				
			print "user exists already and that user is %s" %existing_user.user_name
			u1 = existing_user
		else:
			u1=documents.User()
			u1.fb_uid = user['id']
			#c.id = user['id']
			u1.user_name = user['first_name']
		u1.email = user['email']
                #u1.first().update_one(add_to_set__storeid = request.params['storeid'])
		config['id'] = u1.fb_uid
                u1.access_token = oauth_access_token
                u1.save()
	        u1.reload()
		print "u1.id is %s" %u1.id
		if (config['user'] == "customer"):
			print "scheduing task mytask"			
			mytask.delay(my_parameter=str(u1.id),storeid=str(config['storeid']))              				#docid passed to broker
                        return render ('/gotohomepage.mako')
		if (config['user'] == "merchant"):
                        print "in merchant"
			c.id = user["id"]
			c.name = user["name"]
                        
			return render('/merchant_profile.html')
    def getshops(self):
	print "in merchant"
	c.id =	 request.params["id"]
        try:
        	c.name = documents.Merchant.objects(fb_id = c.id).first().name
	except:
		the_shops = []
		args = dict(myshop = the_shops)
		print args
		return (request.params['callback'] + "(" + json.dumps(args) + ")")
	else:
		the_shops = [str(x.store_name) for x in documents.Merchant.objects(fb_id = c.id)]
		args = dict(myshop = the_shops)
		print args
		return (request.params['callback'] + "(" + json.dumps(args) + ")")
