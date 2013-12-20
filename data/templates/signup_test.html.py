# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1327900596.779167
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/signup_test.html'
_template_uri='/signup_test.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<meta charset="utf-8" />\n<script type="text/javascript" src="http://localhost:5000/jquery.js"> </script>\n<script type="text/javascript" src="http://localhost:5000/all.js"> </script>\n<script type = "text/javascript" src="http://localhost:5000/ursignup.js"> </script>\n<script language = javascript>\n$user_id = ')
        # SOURCE LINE 8
        __M_writer(escape(c.id))
        __M_writer(u'\nalert("logged in user = " + $user_id)\n</script>\n<link rel="stylesheet" href="http://localhost:5000/header.css" media="screen" type="text/css"/>\n<link rel="stylesheet" href="http://localhost:5000/mnbody.css" media="screen" type="text/css"/>\n<style type="text/css">\nhtml       {\n                  background-color: #ddd;\n                  font: 62.5%/1 "Lucida Sans Unicode","Lucida\nGrande",Verdana,Arial,Helvetica,sans-serif;\n          }\n          body { padding: 100px; }\n          #wrapper { text-align: center; }\n          .icon:before { line-height: .7em; }\n</style>\n</head>\n<body>\n<!--  Header -->\n<div id="backwrap" class="bodybg"> <img\nsrc="/home/purvi/Desktop/masti/Preetis... 0619.jpg" height="100"\nwidth="200" border="0" hspace=150 vspace=0 /> <span class="centerDoc">\n <h1>Welcome to Fiesta</h1>\n </span>\n <div id="usrlogin">\n   <h2 style="position:absolute; left:1050px; width:200px;\nheight:40px">Want to share with us</h2>\n   <img style="cursor:pointer"\nsrc="https://dgjcoqnzn763b.cloudfront.net/images/general/btn_fconnect.png"\nonClick="connectToapp()"/>\n   <h2 style="position:absolute; left:1050px; width:200px;\nheight:40px">R u a merchant?</h2>\n   <img style="cursor:pointer"\nsrc="https://dgjcoqnzn763b.cloudfront.net/images/general/btn_fconnect.png"\nonClick="merchantToapp()"/> </div>\n</div>\n<!-- Header ends-->\n<div id="mainbody">\n<div id="main_content">\n <div id="wrapper">\n   <h1>Merchant Registration</h1>\n   <br />\n   <br />\n   <div class="form_section">\n     <div class="field_wrapper">\n       <div class="label_wrapper">\n         <label for="id_name"> Name </label>\n       </div>\n       <input id="id_name"  type="text" name="name" />\n     </div>\n     <!--              <div class="field_wrapper">\n                     <div class="label_wrapper">\n                             <label for="contact">\n                                      Contact No <span\nclass="required">*</span>\n                             </label>\n                     </div>\n                     <input id="contact"  type="text" name="contactno" />\n\n               </div> -->\n     <div class="field_wrapper">\n       <div class="label_wrapper">\n         <label for="storname"> Store Name <span\nclass="required">*</span> </label>\n       </div>\n       <input id="storname"  type="text" name="storename" />\n     </div>\n     <div class="field_wrapper">\n       <div class="label_wrapper">\n         <label for="ttl"> Title <span class="required">*</span> </label>\n       </div>\n       <input id="ttl"  type="text" name="title" />\n     </div>\n     <div class="field_wrapper">\n       <div class="label_wrapper">\n         <label for="site_url"> SiteURL <span\nclass="required">*</span> </label>\n       </div>\n       <input id="site_url"  type="text" name="siteurl" />\n     </div>\n     <div>\n       <input type="button" value="Register with Fiesta"\nonClick="store_merchant_details(storename.value,title.value,siteurl.value)">\n     </div>\n   </div>\n </div>\n </div>\n</div>\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


