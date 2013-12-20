# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332867784.30938
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/stepstointegrate.html'
_template_uri='/stepstointegrate.html'
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
        __M_writer(u'<html>\n<head>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 3
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/shop.css"media="screen" type="text/css"/>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/>\n<meta charset="utf-8" />\n</head>\n<body>\n\n<div id="backwrap" class="bodybg">\n\t\n\t<div id="partners_gep_ab_logged">\n\t<img src="http://')
        # SOURCE LINE 12
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n\n\n\n<div class="right">\n<a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 17
        __M_writer(escape(c.name))
        __M_writer(u'</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        # SOURCE LINE 18
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile?doc_id=')
        __M_writer(escape(c.doc_id))
        __M_writer(u'"  style="text-decoration:none; color: white"> Merchant Profile</a>\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.facebook.com/logout.php?next=http://')
        # SOURCE LINE 19
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'" style="text-decoration:none; color: white"> Logout </a>\n</div>\t\t \n\t   </div> <!-- right close-->\n\t<ul id="nav" class="tabs blue-tabs">\n<li><a href="http://')
        # SOURCE LINE 23
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html"> HOME</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 24
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html"> Social Plugins</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 25
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html"> About Us</a>  </li>\n<li><a href="http://')
        # SOURCE LINE 26
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html"> Contact Us</a>  </li>\n</ul>\n\n\t</div>\n\n<div class="highlights">\n\t\t<div class ="hl_wrapper">\n\t\t\t<div id="mainbody" align="center" >\n\n\t<div id="documentation">\n\t<h1>Integration Instructions</h1><br/>\n\t<p>Get started to integrate with FIESTA</p>\n\t<p>Follow these instructions</p>\n\t<h2>JavaScript Integration</h2>\n\t<p>\n\tCopy and paste this JavaScript code block at the top of the the body section on your order \t\tconfirmation page. \n\t</p>\n\t</div><br/><br/>\n\t\t<div class="box" align="left">\n\t\t\t<div id="L1">\n\t\t\t<span class="o">&lt;</span>\n\t\t\t<span class="nx">script</span>\n\t\t\t<span class="nx">language</span>\n\t\t\t<span class="o">=</span>\n\t\t\t<span>"javascript"</span>\n\t\t\t<span class="nx">type</span>\n\t\t\t<span class="o">=</span>\n\t\t\t<span>"text/javascript"</span>\n\t\t\t<span class="nx">src</span>\n\t\t\t<span class="o">=</span>\n\t\t\t<span>\'http://')
        # SOURCE LINE 56
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/all.js\'</span>\n\t\t\t<span class="o">&gt;&lt;</span>\n\t\t\t<span>/script&gt;</span>\n\t\t\t</div>\n\n\t\t\t<div id="L2">\n\t\t\t<span class="o">&lt;</span>\n\t\t\t<span class="nx">script</span>\n\t\t\t<span class="nx">language</span>\n\t\t\t<span class="o">=</span>\n\t\t\t<span>"javascript"</span>\n\t\t\t<span class="nx">type</span>\n\t\t\t<span class="o">=</span>\n\t\t\t<span>"text/javascript"</span>\n\t\t\t<span class="o">&gt;</span>\n\t\t\t</div>\n\n\t\t\t<div id="L3">\n\t\t\t<span class="nx">init</span>\n\t\t\t<span class="p">(</span>\n\t\t\t<span class="s3">\'')
        # SOURCE LINE 76
        __M_writer(escape(c.doc_id))
        __M_writer(u'\'</span>\n\t\t\t<span class="p">);</span>\n\t\t\t</div>\n\n\t\t\t<div id="L6">\n\t\t\t<span class="o">&lt;</span>\n\t\t\t<span>/script&gt;</span>\n\t\t\t</div>\n\n\t\t\t<div id="L7">\n\t\t\t<span class="o">&lt;</span>\n\t\t\t<span>iframe id = "fiesta_frame" style = "visibility:hidden; display:none" /&gt;\n                        </span>\n\t\t\t</div>\n</div>\n                        </div>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\n\n\n<div class="sc_footer gep_bold">\n      <a href="http://')
        # SOURCE LINE 99
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> |  \n        <a href="http://')
        # SOURCE LINE 100
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html">Social Plugins</a> |  \n        <a href="http://')
        # SOURCE LINE 101
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html">About Fiesta</a> |  \n        <a href="http://')
        # SOURCE LINE 102
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html">Contact Us</a> | \n\n\t<br/ ><br/>    \n       <span class="gep_font10px">*Padmaj*</span>\n</div>\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


