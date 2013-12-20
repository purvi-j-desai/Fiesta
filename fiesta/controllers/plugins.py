import logging
from urllib2 import *
from pylons import request, response, session, config, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import facebook
import json
from fiesta.lib.base import BaseController, render
from documents import *
log = logging.getLogger(__name__)

 
class PluginsController(BaseController):

    def celebrations(self):
	c.doc_id = request.params['doc_id']
	c.storeid = c.doc_id
	print 'Celebration : User will get notified on important events of his/her relatives' 
        return render('/celebrations.mako')  
	
    def paisan(self):
	print 'Paisan : User can like the facebook page of the merchant'
	c.doc_id = request.params['doc_id']
        c.siteurl=Merchant.objects(id = c.doc_id).first().site_url
        return render('/paisan.mako')  

    def saltation(self):
	c.doc_id = request.params['doc_id']
  	print 'Saltation : User can share his/her shopping experience with friends through FB share or post 		on wall'
        return render('/saltation.mako')

    def setpluginurl(self):
	c.doc_id = request.params['doc_id']
        print "mid - %s" %c.doc_id
        if request.params['plugin1'] == 'true':
		print "plugin 1"
		set_url = 'http://'+config['myhost']+':5000/plugins/celebrations'
		Merchant.objects(id = c.doc_id).update_one(add_to_set__plugin_urls = set_url)
	if request.params['plugin2'] == 'true':
		set_url = 'http://'+config['myhost']+':5000/plugins/paisan'
		Merchant.objects(id = c.doc_id).update_one(add_to_set__plugin_urls = set_url)
	if request.params['plugin3'] == 'true':
		set_url = 'http://'+config['myhost']+':5000/plugins/saltation'
		Merchant.objects(id = c.doc_id).update_one(add_to_set__plugin_urls = set_url)


    def removepluginurl(self):
	c.doc_id = request.params['doc_id']
        c.id = Merchant.objects(id = c.doc_id).first().fb_id
	c.store_name = Merchant.objects(id = c.doc_id).first().store_name
	
	if request.params['plugin1'] == 'true':
		print "plugin 1"
		is_celebrations = 'false'
		set_url = 'http://'+config['myhost']+':5000/plugins/celebrations'
                if set_url in Merchant.objects(id = c.doc_id).first().plugin_urls:
			Merchant.objects(id = c.doc_id).update_one(pull__plugin_urls = set_url)
	if request.params['plugin2'] == 'true':
		is_paisan = 'false'
		set_url = 'http://'+config['myhost']+':5000/plugins/paisan'
		if set_url in Merchant.objects(id = c.doc_id).first().plugin_urls:
			Merchant.objects(id = c.doc_id).update_one(pull__plugin_urls = set_url)
	if request.params['plugin3'] == 'true':
		is_saltation = 'false'
		set_url = 'http://'+config['myhost']+':5000/plugins/saltation'
		if set_url in Merchant.objects(id = c.doc_id).first().plugin_urls:
			Merchant.objects(id = c.doc_id).update_one(pull__plugin_urls = set_url)
	#c.myplugins = dict(celebrations=is_celebrations, saltation=is_saltation, 				paisan=is_paisan)
	redirect(url(controller='retailer', action='showshopinfo', fbid = c.id, store = c.store_name))
        
    def geturl(self):
	print "hitting"
        c.doc_id = request.params['doc_id']
	next_url = Merchant.objects(id = c.doc_id).first().plugin_urls[0]
	Merchant.objects(id = c.doc_id).update_one(pull__plugin_urls = next_url)
        Merchant.objects(id = c.doc_id).update_one(push__plugin_urls = next_url)
	next_url = next_url+"?doc_id="+c.doc_id
       	args = dict(nexturl = next_url)
	print args
        #args = 
	return (request.params['callback'] + "(" + json.dumps(args) + ")")
