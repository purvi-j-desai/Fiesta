import logging
from merchantstoretask import merchanttask
from pylons import request, response, session, config, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import json
from fiesta.lib.base import BaseController, render
from documents import *
import facebook
from sendmailtask import mailtask
log = logging.getLogger(__name__)

class RetailerController(BaseController):

	def signup(self):
		c.name = request.params['name']
		c.id = request.params['id']
		return render ('/merchant_signup.html')
	def store(self):
        	print "in retailer store %s" %request.params['id']
                c.id = request.params['id']
		c.name = User.objects(fb_uid = c.id).first().user_name
		c.email = User.objects(fb_uid = c.id).first().email
                c.store = request.params['store']
                m = Merchant(fb_id = c.id)
		m.save()
                c.doc_id = m.id
               
                merchanttask.delay(str(c.doc_id), str(request.params['site']), str(request.params['title']), 			str(request.params['contact']), 
                str(request.params['store']))
            	print "end retailer"
                return render ('/signupsuccess.html')
		
		'''m = Merchant(fb_id = request.params['id'])
                m.site_url = request.params['site']
                m.dealer_in = request.params['title']
                m.phone_no = request.params['contact']
                m.store_name = request.params['store']
                m.save()
                return render ('/plugins.html')'''

	def email_instruction(self):
 		send_to = request.params['email']
		#mid = request.params['fbid']
		#storename = request.params['store']
		#doc_id = Merchant.objects(Q(fb_id = mid) & Q(store = storename)).first().id
		print "send to %s" %send_to
		msg = '''Dear Customer the instructions are as follows:
		Copy and paste this JavaScript code block at the top of the the body section on your order 			confirmation page.
		< script language = "javascript" type = "text/javascript" src = 		'https://192.168.1.1:5000/js/all.js' >< /script>
		< script language = "javascript" type = "text/javascript" >
		init ( 'doc_id' );
		< /script>
		< iframe id = "fiesta_frame" style = "visibility:hidden; display:none" />
		'''
                mailtask.delay(send_to, "", msg)
                #call task to mail---also construct the message with instructions 
	def show_me_instruction(self):
                c.id = request.params['mid']
                c.store_name = request.params['store']
                c.name = Merchant.objects(fb_id = c.id).first().name
		c.doc_id = Merchant.objects(Q(fb_id = c.id) & Q(store_name=c.store_name)).first().id
                return render ('/stepstointegrate.html') 

	def redirectplugin(self):
                
                c.doc_id = request.params['doc_id']
                c.name = Merchant.objects(id=c.doc_id).first().name
		c.store_name = Merchant.objects(id=c.doc_id).first().store_name
		return render ('/plugins.html')

	def redirectintegrate(self):
		c.doc_id = request.params['doc_id']
		#m = Merchant.objects(fb_id = c.id).first()
		#c.doc_id = m.id
        	c.name = Merchant.objects(id=c.doc_id).first().name
                c.id = Merchant.objects(id = c.doc_id).first().fb_id
		c.store_name = Merchant.objects(id=c.doc_id).first().store_name
		print "In redirect-integrate c.doc_id: %s" %c.doc_id
		return render ('/integrate.html')
               
        def showshopinfo(self): #loads after profile page
		m=Merchant.objects(Q(fb_id = request.params['fbid']) & Q(store_name=request.params	['store'])).first()  
                c.name = m.name
		c.store_name = m.store_name
		c.doc_id = m.id
                c.id = m.fb_id
		c.site_url = m.site_url  
                c.plugincount = len(m.plugin_urls) 
        	#################################
	     	c.merchant_plugin_urls = m.plugin_urls
		is_celebrations = 'false'
		is_saltation = 'false'
		is_paisan = 'false'
        	for x in c.merchant_plugin_urls:
			if ('saltation' in x):
				is_saltation = 'true'
			if ('celebrations' in x):
				is_celebrations = 'true'
			if ('paisan' in x):
				is_paisan = 'true'
     		c.myplugins = dict(celebrations=is_celebrations, saltation=is_saltation, 			paisan=is_paisan)  
		c.mydump = json.dumps( c.merchant_plugin_urls )
		print  c.mydump 
		print c.myplugins
		#################################
		return render ('/editprofile.html')

	def showshopplugins(self): #not called
		c.doc_id=request.params['docid']
		c.merchant_plugin_urls = Merchant.objects(id = str(c.doc_id)).first().plugin_urls
		is_celebrations = 'false'
		is_saltation = 'false'
		is_paisan = 'false'
        	for x in c.merchant_plugin_urls:
			if ('saltation' in x):
				is_saltation = 'true'
			if ('celebrations' in x):
				is_celebrations = 'true'
			if ('paisan' in x):
				is_paisan = 'true'
		c.plugincount = len(c.merchant_plugin_urls)
     		c.myplugins = dict(celebrations=is_celebrations, saltation=is_saltation, 			paisan=is_paisan)  
		c.mydump = json.dumps( c.merchant_plugin_urls )
		print  c.mydump 
		print c.myplugins  
		return render ('/showshopplugins.html')
        
	def showprofile(self):
		c.id = config['id']
                print "fb_id is %s" %c.id
                try:
			c.name = Merchant.objects(fb_id=c.id).first().name
                except AttributeError:
		        c.shopcount = 0
			c.name = User.objects(fb_uid=c.id).first().user_name
			return render('/merchant_profile.html')         
		else:	
                	c.shop = []
			for m in Merchant.objects(fb_id = c.id):
				c.shop.append(m.store_name)
                	json.dumps(c.shop)
			c.shopcount = len(c.shop)
			return render('/merchant_profile.html')         
