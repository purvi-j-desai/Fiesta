# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333119512.512971
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/merchant_signup.html'
_template_uri='/merchant_signup.html'
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
        __M_writer(u'<html>\n<head>\n<title> Fiesta : Merchant Signup </title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<script src="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/menuscript.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 6
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n<link rel="stylesheet" href="http://')
        # SOURCE LINE 7
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/menustyle.css"media="screen" type="text/css"/> \n\n<script src="http://')
        # SOURCE LINE 9
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/all.js"></script>\n<style type="text/css">\n\n#labelf {font-family : garamond, times; font-size: 10px }\n</style>\n\n</head>\n<body>\n\n<div id="backwrap" class="bodybg">\n\t\n\t<div id="partners_gep_ab_logged">\n\t<img src="http://')
        # SOURCE LINE 21
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n<div class="right">\n<a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 23
        __M_writer(escape(c.name))
        __M_writer(u'</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        # SOURCE LINE 24
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile?doc_id=')
        __M_writer(escape(c.id))
        __M_writer(u'"  style="text-decoration:none; color: white"> Merchant Profile</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.facebook.com/logout.php?next=http://')
        # SOURCE LINE 25
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'" style="text-decoration:none; color: white"> Logout </a>\n</div>\t \n\t   </div> <!-- right close-->\n\t<ul id="nav" class="tabs blue-tabs">\n<li><a href="http://')
        # SOURCE LINE 29
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html"> HOME</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 30
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html"> Social Plugins</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 31
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html"> About Us</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 32
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html"> Contact Us</a>  </li>\n</ul>\n\n\t</div>  <!-- menu divider close-->\n\n\t<div class="highlights">\n\t\t<div class ="hl_wrapper">\n\t\t\t\n\n<div id="mainbody">\n<br>\n <h1 align="center" >Merchant Registration for ')
        # SOURCE LINE 43
        __M_writer(escape(c.name))
        __M_writer(u'</h1>\t\n\t<br /><br />\n\n              \n<div id="labelf">\n <form name="Signup" id="addmerchant">\n\t<table width="80%" border="0" cellspacing="1" cellpadding="1" style="border:0px; color: #000000;" align="center" color="black">\n\t\n\t\t\t<tr> <th align="left">  <label for="Contact No: " >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contact No:</span> <span class="required"> * </span> </label></th> <td> <input type="text" name="contact" /></td> </tr>\n\t\t<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n\t<tr> <th align="left">  <label for="Store Name: ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store Name:<span class="required"> *</span></label></th> <td><input type="text" name="storename" /> </td> </tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n\t<tr> <th align="left">  <label for="Title: ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dealer In: <span class="required"> * </span> </label> </th> <td><input type="text" name="mtitle" /></td> </tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n\t<tr> <th align="left">  <label for="Site ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SiteURL: <span class="required"> * </span> </label> </th> <td><input type="text" name="site" /></td> </tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n\t<tr> <td>  </td><td><button onclick="passRetailerInfo(contact.value,storename.value,mtitle.value,site.value, ')
        # SOURCE LINE 61
        __M_writer(escape(c.id))
        __M_writer(u')" id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B;" type="button">Register with Fiesta</button> \n<!--\n<a target="" onmouseout="setOutImg(\'3\',\'\');" onmouseover="setOverImg(\'3\',\'\');" href="passRetailerInfo(contact.value,storename.value,mtitle.value,site.value, ')
        # SOURCE LINE 63
        __M_writer(escape(c.id))
        __M_writer(u')">\n<img id="button1" vspace="1" hspace="1" border="0" src="http://')
        # SOURCE LINE 64
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/buttons/button3up.png">\n</a>\n-->\n</td> </tr>\n<tr><th></th><td> </td><td> </td> </tr>\t<tr><th></th><td> </td><td> </td></tr>\t<tr><th></th><td> </td><td> </td></tr>\n</div>\n\n\t</table>\n\t </form>\n\n\t</div>\n\n      </div><!-- end form wrapper-->\n\n\n\n</div><!-- end wrapper-->\n\n\n\n     </div>\t<!-- hl-wrapper close-->\n   </div>\t<!-- highlights close-->\n   </div>   <!--  backwrap-->\n\n\n<div class="sc_footer gep_bold">\n      <a href="http://192.168.1.1:5000/homepage.html">Home</a> |  \n        <a href="http://192.168.1.1:5000/socialplugin.html">Social Plugins</a> |  \n        <a href="http://192.168.1.1:5000/AboutUs.html">About Fiesta</a> |  \n        <a href="http://192.168.1.1:5000/contactus.html">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


