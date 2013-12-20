# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332808422.312279
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/editprofile.html'
_template_uri='/editprofile.html'
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
        __M_writer(u'<html>\n<head>\n<title>Edit profile</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<script type="text/javascript" src="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery-1.7.1.min.js"></script>\n<script type="text/javascript" src="http://')
        # SOURCE LINE 6
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery-ui-1.8.17.custom.min.js"></script>\n<script type="text/javascript" src="http://')
        # SOURCE LINE 7
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.lightbox-0.5.js"></script>\n<link rel="stylesheet" type="text/css" href="http://')
        # SOURCE LINE 8
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/style-projects-jquery.css" />\n<link rel="stylesheet" type="text/css" href="http://')
        # SOURCE LINE 9
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/jquery.lightbox-0.5.css" media="screen" />\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 10
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/>\n<link type="text/css" href="http://')
        # SOURCE LINE 11
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/smoothness/jquery-ui-1.8.17.custom.css" rel="stylesheet" />\n<script type="text/javascript">\n\t$(document).ready(function(){\n\t\n\t\t\t\t// Tabs\n\t\t\t\t$(\'#tabs\').tabs();\n                 \t       \n//\t\t\t\talert("before if")\n//\t\t\t\talert(\'')
        # SOURCE LINE 19
        __M_writer(escape(c.plugincount))
        __M_writer(u"')\n\t\t\t\t\n\t\t\t\tif(")
        # SOURCE LINE 21
        __M_writer(escape(c.plugincount))
        __M_writer(u'==0)\n\t\t\t\t{\n\t\t\t\t  $(\'#id_send_button\').hide();\n\t\t\t\t  $("span[title=\'nop\']").append("You have no plugins.");\n\t\t\t\t}\n\t\t\t\t$(\'#salt\').hide();\n\t\t\t\t$(\'#paisan\').hide();\n\t\t\t\t$(\'#celeb\').hide();\n\t\t\t\t\n\t\t\t\t\n\t\t\t\tif (')
        # SOURCE LINE 31
        __M_writer(escape(c.myplugins['celebrations']))
        __M_writer(u'==true) {\t\n\t\t\t\t\t$(\'#celeb\').show();\n\t\t\t\t\t//alert("1");\n\t\t\t\t}\n\t\t\t\tif (')
        # SOURCE LINE 35
        __M_writer(escape(c.myplugins['saltation']))
        __M_writer(u'==true)\t{\n\t\t\t\t\t//alert("2");\n\t\t\t\t\t$(\'#salt\').show();\n\t\t\t\t}\n\t\t\t\tif (')
        # SOURCE LINE 39
        __M_writer(escape(c.myplugins['paisan']))
        __M_writer(u'==true)\t{\n\t\t\t\t\t$(\'#paisan\').show();\n\t\t\t\t\t//alert("3");\n\t\t\t\t}\n\t\t\t\t\n    });\n\t\t\tfunction removeplugins(){\n\t\t\t\tvar url;\n//\t\t\t\t alert(\'hello\');\n \t\t\t\t\turl = "http://')
        # SOURCE LINE 48
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/plugins/removepluginurl?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'&"\n\t\t\t\t\t if(document.getElementById(\'celebrations\').checked)\n\t\t\t\t\t\turl = url + "plugin1=true"\n\t\t\t\t\t else\n\t\t\t\t\t\turl = url + "plugin1=false"\n\t\t\t\t\t        url = url + "&"\n\t\t\t\t\t if(document.getElementById(\'paisan\').checked)\n\t\t\t\t\t \turl = url + "plugin2=true"\n\t\t\t\t\t else\n\t\t\t\t\t\turl = url + "plugin2=false"\n                    \t\t\t\turl = url + "&"\n\t\t\t\t\t if(document.getElementById(\'saltation\').checked)\n\t\t\t\t\t \turl = url + "plugin3=true"\n\t\t\t\t\t else\n\t\t\t\t\t\turl = url + "plugin3=false"\n\t\t\t\t\t\talert(\'url : \'+url);\n\t\t\t\t\t\tjQuery.get(url);\n\t\t\t\t\t\t//alert(\'got url\');\t\n\t\t\t\t\t\talert(\'Removed Successfully!\')\t\n\t\t\t\t\t\n\t\t\t\t\t}\n\n</script>\n<style type="text/css">\n\t\t\t.demoHeaders { margin-top: 2em; }\n\t\t\t#dialog_link {padding: .4em 1em .4em 20px;text-decoration: none;position: relative;}\n\t\t\t#dialog_link span.ui-icon {margin: 0 5px 0 0;position: absolute;left: .2em;top: 50%;margin-top: -8px;}\n\t\t\tul#icons {margin: 0; padding: 0;}\n\t\t\tul#icons li {margin: 2px; position: relative; padding: 4px 0; cursor: pointer; float: left;  list-style: none;}\n\t\t\tul#icons span.ui-icon {float: left; margin: 0 4px;}\n</style>\n</head>\n<body>\n<div id="backwrap" class="bodybg">\n\n    <div id="partners_gep_ab_logged"> <img src="http://')
        # SOURCE LINE 83
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n      <div class="right"> <a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 84
        __M_writer(escape(c.name))
        __M_writer(u'</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile"  style="text-decoration:none; color: white">Merchant Profile</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href=\'https://www.facebook.com/logout.php?next=http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'\' style="text-decoration:none; color: white"> Logout </a> </div>\n      <!--Hit controller -->\n    </div>\n    <!--logged close-->\n    <ul id="nav" >\n      <li> <a href="http://')
        # SOURCE LINE 89
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> </li>\n      <li> <a href="www.rediffmail.com">Intro Video</a> </li>\n      <li> <a href="www.rediffmail.com">How it works?</a> </li>\n      <li> <a href="www.rediffmail.com">Contact Us</a> </li>\n    </ul>\n\n  </div>\n\n<!-- menu divider close-->\n<div class ="highlights">\n<div class ="hl_wrapper">\n\n  <div id="tabs">\n    <ul>\n      <li><a href="#tabs-1">Settings</a></li>\n      <li><a href="#tabs-2">Plugins</a></li>\n      <li><a href="#tabs-3">Integration</a></li>\n    </ul>\n    <div id="tabs-1">\n      <h1>Shop details:</h1>\n      <!--<h2>Partner ID : ')
        # SOURCE LINE 109
        __M_writer(escape(c.doc_id))
        __M_writer(u'</h2>\n                                         <h2>Store : ')
        # SOURCE LINE 110
        __M_writer(escape(c.store_name))
        __M_writer(u'</h2>\n                                         <h2>URL : ')
        # SOURCE LINE 111
        __M_writer(escape(c.site_url))
        __M_writer(u'</h2>-->\n      <div class="divTable">\n        <div class="divRow">\n          <div class="divCell" align="center">Partner ID</div>\n          <div  class="divCell">')
        # SOURCE LINE 115
        __M_writer(escape(c.doc_id))
        __M_writer(u'</div>\n        </div>\n        <div class="divRow">\n          <div class="divCell" align="center">Store</div>\n          <div  class="divCell">')
        # SOURCE LINE 119
        __M_writer(escape(c.store_name))
        __M_writer(u'</div>\n        </div>\n        <div class="divRow">\n          <div class="divCell" align="center">URL</div>\n          <div  class="divCell">')
        # SOURCE LINE 123
        __M_writer(escape(c.site_url))
        __M_writer(u'</div>\n        </div>\n      </div>\n    </div><!--tab-1 end-->\n\t\n\t\n    <div id="tabs-2">\n      <div class="highlights">\n        <div class ="hl_wrapper">\n          <div id="mainbody" >\n            <h1 align="center" >Your selected plugins:</h1>\n            <br />\n            <br />\n            <div id="gallery" align="center"> <span title="nop"></span>\n              <div id="salt">\n                <div class="widget_box" style="height:40%;width:13%;" align="center"> <a href="http://')
        # SOURCE LINE 138
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/finalshare.png" title="Post On Wall">\n                  <div class="widget_title">Saltation</div>\n                  <img src="http://')
        # SOURCE LINE 140
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/postOnwall.png" height="95" width="120"/> </a>\n                  <input type="checkbox" id="saltation" value="saltation" />\n                  Saltation </div>\n              </div>\n              <div id="paisan">\n                <div class="widget_box" style="height:40%;width:13%;"> <a href="http://')
        # SOURCE LINE 145
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/finalmail.png" title="Become a FAN">\n                  <div class="widget_title">Paisan</div>\n                  <img src="http://')
        # SOURCE LINE 147
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/like.png" height="95" width="120"/> </a>\n                  <input type="checkbox" id="paisan" value="paisan" />\n                  Paisan </div>\n              </div>\n              <div id="celeb">\n                <div class="widget_box" style="height:40%;width:13%;"> <a href="http://')
        # SOURCE LINE 152
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/finalmail.png" title="Have a mail on Spacial Events">\n                  <div class="widget_title">Celebration</div>\n                   <img src="http://')
        # SOURCE LINE 154
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/events.jpeg" height="95" width="120"/>\n\t\t\t\t  </a>\n\t\t\t\t  \n                  <input type="checkbox" id="celebrations" value="celebrations" />\n                  Celebrations </div><!--widget box close-->\n              </div> <!-- end celeb-->\n             \n            </a>\n              <!--<a href="http://')
        # SOURCE LINE 162
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/redirectintegrate?mid=')
        __M_writer(escape(c.id))
        __M_writer(u'"> -->\n            </div>\n <button onClick="removeplugins()" id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B; float: right; margin: 30 100 0" type="button">Remove plugins</button>\n\t\t\t  \n\t\t\t   <a href="http://')
        # SOURCE LINE 166
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/redirectplugin?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'">\n            <button id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: white; background-color: #3B899B; float: right; margin: 0 100 0" type="button">Add plugins</button>\n            <!--end gallery-->\n            </div>\n          <!-- MAINBODY-->\n        </div>\n        <!-- hl-wrapper close-->\n      \n     \n    </div> <!-- highlights close-->\n\t</div><!--tab2 end-->\n\t\n\n    <div id="tabs-3">\n      <div class="highlights" style="height: 90%">\n        <div class ="hl_wrapper">\n          <div id="mainbody" align="center">\n            \n            <div class="integration_option" id="id_email_widget_root">\n              <form>\n                <div class ="form_section">\n                  <div class="option_title gep_txtcenter gep_margin_btm10px">Email instructions to my \t\t\t\t\ttechnical team </div>\n                  <div style ="text-align: center; margin-bottom: 10px;" class="field_wrapper">\n                    <div class="gep_txtcenter"><img src="http://')
        # SOURCE LINE 189
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/email-instructions.jpg"></div>\n                    <div class="gep_font14px">Enter Email Address</div>\n                    <input type="text" value="" style="width: 190px; padding: 3px;" id="id_email_inputbox" name = "email">\n                  </div><!--field wrapper end-->\n                  <div class="gep_txtcenter">\n                    <button type="button" style="font-size: 17px ! important; width: 200px; padding: 4px; font-weight: normal ! important;" id="id_send_button"  onclick = "sendmail(email.value)">Email Instructions</button>\n                  </div><!--gep txtcenter-->\n                </div>\n              </form>\n\t\t\t  </div>\n\t\t\t \n              <div class="integration_option">\n                <div class="option_title gep_txtcenter gep_margin_btm10px">Show me instructions to integrate</div>\n                <div style="height: 150px;" class="gep_txtcenter"><img src="http://')
        # SOURCE LINE 202
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/show-instructions.jpg"></div>\n                <div class="gep_txtcenter" style="margin: 25px 0pt 10px;"> <a href="http://')
        # SOURCE LINE 203
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/show_me_instruction?mid=')
        __M_writer(escape(c.id))
        __M_writer(u'&store=')
        __M_writer(escape(c.store_name))
        __M_writer(u'" >\n                  <button  style="font-size: 17px ! important; width: 200px; padding: 4px; font-weight: normal ! important;" type="button">See Instructions</button>\n                  </a> </div>\n              </div><!--end integration section -->\n            </div>            <!--end integgration-->\n          </div>          <!-- mainbody close-->\n        </div>        <!-- hlwrapper close-->\n      </div>      <!-- highlights close-->\n    \n    <!-- tab3 close-->\n  \n  </div><!-- tabs end-->\n</div>\n</div>\n</div>\n\n<div class="sc_footer gep_bold">\n      <a href="http://')
        # SOURCE LINE 220
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> |  \n        <a href="file:///F|/project/fiesta/fiesta/templates/www.rediffmail.com">Intro Video</a> |  \n        <a href="file:///F|/project/fiesta/fiesta/templates/www.rediffmail.com">How it works?</a> |  \n        <a href="file:///F|/project/fiesta/fiesta/templates/www.rediffmail.com">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


