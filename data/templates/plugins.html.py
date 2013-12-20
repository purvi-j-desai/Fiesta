# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332866262.823998
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/plugins.html'
_template_uri='/plugins.html'
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
        __M_writer(u'<html>\n<head>\n<title> Fiesta: Plugins</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/jquery.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n<script type="text/javascript">\n\nfunction selectplugins()\n{\n var url;\n //alert(\'hello\');\n url = "http://')
        # SOURCE LINE 12
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/plugins/setpluginurl?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'&"\n if(document.getElementById(\'celebrations\').checked)\n\turl = url + "plugin1=true"\n else\n\turl = url + "plugin1=false"\n url = url + "&"\n if(document.getElementById(\'paisan\').checked)\n \turl = url + "plugin2=true"\n else\n\turl = url + "plugin2=false"\n url = url + "&"\n if(document.getElementById(\'saltation\').checked)\n \turl = url + "plugin3=true"\n else\n\turl = url + "plugin3=false"\n //alert(\'url : \'+url);\n jQuery.get(url, function() { alert ("success")} );\n alert(\'Selected Plugin Added!\');\n}\n\n</script>\t\n<style type="text/css">\n\t\t\t.demoHeaders { margin-top: 2em; }\n\t\t\t#dialog_link {padding: .4em 1em .4em 20px;text-decoration: none;position: relative;}\n\t\t\t#dialog_link span.ui-icon {margin: 0 5px 0 0;position: absolute;left: .2em;top: 50%;margin-top: -8px;}\n\t\t\tul#icons {margin: 0; padding: 0;}\n\t\t\tul#icons li {margin: 2px; position: relative; padding: 4px 0; cursor: pointer; float: left;  list-style: none;}\n\t\t\tul#icons span.ui-icon {float: left; margin: 0 4px;}\n</style>\t\n</head>\n<body>\n\n<div id="backwrap" class="bodybg">\n\t\n\t<div id="partners_gep_ab_logged">\n\t<img src="http://')
        # SOURCE LINE 47
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n\n\n\n<div class="right">\n<a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 52
        __M_writer(escape(c.name))
        __M_writer(u'</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        # SOURCE LINE 53
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'"  style="text-decoration:none; color: white"> Merchant Profile</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.facebook.com/logout.php?next=http://')
        # SOURCE LINE 54
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'" style="text-decoration:none; color: white"> Logout </a>\n</div>\t\t \n\t   </div> <!-- right close-->\n\t<ul id="nav" class="tabs blue-tabs">\n<li><a href="http://')
        # SOURCE LINE 58
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html"> HOME</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 59
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html"> Social Plugins</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 60
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html"> About Us</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 61
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html"> Contact Us</a>  </li>\n</ul>\n\n</div>\n\n\t<div class="highlights">\n\t\t<div class ="hl_wrapper">\n\t\t\t<div id="mainbody" align="center">\n\t\t\t<h1 align="center" >Select plugins</h1>\t<br /><br />\n\t\t\t<img src=\'http://')
        # SOURCE LINE 70
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/images/events.jpeg' />\n\t\t\t<a>&nbsp;&nbsp;&nbsp;&nbsp;</a>\n\t\t\t<img src='http://")
        # SOURCE LINE 72
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/images/like.png' />\n\t\t\t<a>&nbsp;&nbsp;&nbsp;&nbsp;</a>\n\t\t\t<img src='http://")
        # SOURCE LINE 74
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/postOnwall.png\' />\n\t\t\t<br>\n\t\t\t<input type="checkbox" id="celebrations" value="celebrations" />Celebrations\n\t\t\t<a>&nbsp;&nbsp;&nbsp;&nbsp;</a>\n\t\t\t<input type="checkbox" id="paisan" value="paisan" />Paisan\n\t\t\t<a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>\n\t\t\t<input type="checkbox" id="saltation" value="saltation" />Saltation\n\t\t\t<br><br>\n\t\t\t<button onclick="selectplugins()" id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B;" type="button">Select plugins</button>\n\t\t\t<br><br>\n\t\t\t<a href="http://')
        # SOURCE LINE 84
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/redirectintegrate?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'">\n\t\t\t<button id="id_proceed" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B;" type="button">Proceed to Integration</button>\n\t\t\t\n\t\t\t</a>\n\n\n\t\t\t</div><!-- MAINBODY-->\n\n    \t\t </div>\t<!-- hl-wrapper close-->\n     </div>\t<!-- highlights close-->\n   </div>   <!--  backwrap-->\n\n<div class="sc_footer gep_bold">\n      <a href="http://')
        # SOURCE LINE 97
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> |  \n        <a href="http://')
        # SOURCE LINE 98
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html">Social Plugins</a> |  \n        <a href="http://')
        # SOURCE LINE 99
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html">About Fiesta</a> |  \n        <a href="http://')
        # SOURCE LINE 100
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


