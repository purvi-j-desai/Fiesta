# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332858665.97715
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/signupsuccess.html'
_template_uri='/signupsuccess.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title> Fiesta: signupSuccess</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n</head>\n<body>\n\n<div id="backwrap" class="bodybg">\n\t\n\t<div id="partners_gep_ab_logged">\n\t<img src="http://')
        # SOURCE LINE 12
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n\n<div class = right>\n\t<a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 15
        __M_writer(escape(c.name))
        __M_writer(u'</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        # SOURCE LINE 16
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile"  style="text-decoration:none; color: white">Merchant Profile</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href=\'https://www.facebook.com/logout.php?next=http://')
        # SOURCE LINE 17
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'\' style="text-decoration:none; color: white"> Logout </a>\n\t</div>\n\t \n\t   </div> <!-- right close-->\n\t<ul id="nav" class="tabs blue-tabs">\n<li><a href="http://')
        # SOURCE LINE 22
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html"> HOME</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 23
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html"> Social Plugins</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 24
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html"> About Us</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 25
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html"> Contact Us</a>  </li>\n</ul>\n\n\t</div>  <!-- menu divider close-->\n\n<div class="highlights">\n\t\t<div class ="hl_wrapper">\n\t\t\t<div id="mainbody" align="center">\n\t<h1>\n\tCongratulations ')
        # SOURCE LINE 34
        __M_writer(escape(c.name))
        __M_writer(u'! You have successfully activated\n\t<br>\n\tFiesta for "')
        # SOURCE LINE 36
        __M_writer(escape(c.store))
        __M_writer(u'".\n\t</h1>\n\t\t<div class="gep_margin_left7px">\n\t\t<p class="gep_font14px gep_margin_top20px">The next step is to integrate ShopSocially into the order confirmation page of your store.</p>\n\t\t<p class="gep_font14px gep_margin_top10px">You will need your store\'s Account ID to complete the next step.</p>\n\t\t<p class="gep_font14px gep_margin_top20px">\n\t\tAccount ID:\n\t\t<b class="gep_grey">')
        # SOURCE LINE 43
        __M_writer(escape(c.doc_id))
        __M_writer(u'</b>\n\t\t</p>\n\t\t<p class="gep_font14px gep_margin_top20px">\n\t\tYour Account ID has been emailed to\n\t\t<i>')
        # SOURCE LINE 47
        __M_writer(escape(c.email))
        __M_writer(u'</i>\n\t\twith integration instructions.\n\t\t</p>\n\t\t<a href="http://')
        # SOURCE LINE 50
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/redirectplugin?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'">\n<button id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B;" type="button">\nProceed</button>\n</a>\n\t</div>\n        </div>\n</div>\n</div>\n\n\n<div class="sc_footer gep_bold">\n      <a href="http://')
        # SOURCE LINE 61
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> |  \n        <a href="http://')
        # SOURCE LINE 62
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html">Social Plugins</a> |  \n        <a href="http://')
        # SOURCE LINE 63
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html">About Fiesta</a> |  \n        <a href="http://')
        # SOURCE LINE 64
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


