# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332859242.628397
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/integrate.html'
_template_uri='/integrate.html'
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
        __M_writer(u'<html>\n<head>\n<title> Fiesta: Integrate</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<script src="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/all.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 6
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n</head>\n<body>\n\n<div id="backwrap" class="bodybg">\n\n    <div id="partners_gep_ab_logged"> <img src="http://')
        # SOURCE LINE 12
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n      <div class="right"> <a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 13
        __M_writer(escape(c.name))
        __M_writer(u'</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile"  style="text-decoration:none; color: white">Merchant Profile</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href=\'https://www.facebook.com/logout.php?next=http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'\' style="text-decoration:none; color: white"> Logout </a> </div>\n      <!--Hit controller -->\n    </div>\n    <!--logged close-->\n    <ul id="nav" class="tabs blue-tabs">\n<li><a href="http://192.168.1.1:5000/homepage.html"> HOME</a>  </li>\n<li><a href="http://192.168.1.1:5000/socialplugin.html"> Social Plugins</a>  </li>\n<li><a href="http://192.168.1.1:5000/AboutUs.html"> About Us</a>  </li>\n<li><a href="http://192.168.1.1:5000/contactus.html"> Contact Us</a>  </li>\n</ul>\n\n\n  </div>\n\n\n\t<div class="highlights">\n\t\t<div class ="hl_wrapper">\n\t\t\t<div id="mainbody" align="center">\n<h1>\n\tIntegrate with Fiesta\n\t<br>\n\n\t</h1>\n<div class="integration_option" id="id_email_widget_root">\n\t<div class="form_section">   \n\t<div class="option_title gep_txtcenter gep_margin_btm10px">Email instructions to my technical team  \n</div>   \n <div style="text-align: center; margin-bottom: 10px;" class="field_wrapper">       <br/>\n\t<div class="gep_txtcenter"><img src="http://')
        # SOURCE LINE 41
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/ama026.gif" height="20%" width="30%"></div>       <br/>\n\t\t\t\t<div class="gep_font14px">Enter Email Address</div> <form> <input type="text" value="" style="width: 190px; padding: 5px;" id="id_email_inputbox" name = "email">\n</div>  \n<div class="gep_txtcenter" style="margin: 5px 0pt;">   <button type="button" style="font-size: 17px ! important; width: 200px; padding: 8px; font-weight: normal ! important;" id="id_send_button"  onclick = "sendmail(email.value)">Email Instructions</button></div></div>\n</div>\n</form>\n<div class="integration_option">\n        <div class="option_title gep_txtcenter gep_margin_btm10px">Show me instructions to integrate</div>\n        <div style="height: 150px;" class="gep_txtcenter"><marquee WIDTH=35% BEHAVIOR=ALTERNATE><img src="http://')
        # SOURCE LINE 49
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/show-instructions.jpg" style="filter:alpha(opacity=50)"></marquee></div>\n        <div class="gep_txtcenter" style="margin: 15px 0pt 10px;">\n\t    <a href="http://')
        # SOURCE LINE 51
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/show_me_instruction?mid=')
        __M_writer(escape(c.id))
        __M_writer(u'&store=')
        __M_writer(escape(c.store_name))
        __M_writer(u'"><button style="font-size: 17px ! important; width: 200px; padding: 8px; font-weight: normal ! important;" type="button">See Instructions</button></a>\n        </div>\n    </div>\n</div>\n\n     </div>\t<!-- hl-wrapper close-->\n     </div>\t<!-- highlights close-->\n   </div>   <!--  backwrap-->\n</div>\n<div class="sc_footer gep_bold">\n      <a href="http://192.168.1.1:5000/homepage.html">Home</a> |  \n        <a href="http://192.168.1.1:5000/socialplugin.html">Social Plugins</a> |  \n        <a href="http://192.168.1.1:5000/AboutUs.html">About Fiesta</a> |  \n        <a href="http://192.168.1.1:5000/contactus.html">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


