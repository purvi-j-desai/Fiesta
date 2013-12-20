# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1329521226.584984
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/showshopplugins.html'
_template_uri='/showshopplugins.html'
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
        iter = context.get('iter', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title> Fiesta : Merchant Profile</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n<script src="http://')
        # SOURCE LINE 6
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/all.js"></script>\n<style type="text/css">\n\n#labelf {font-family : garamond, times; font-size: 10px }\n</style>\n\n\n\n\n<script type = "text/javascript">\n\t\n\n\t')
        # SOURCE LINE 18
 
        i = iter( c.merchant_plugin_urls )      
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 20
        __M_writer(u'\n\talert("happening..");\n        var mylist = eval \'(\' + ')
        # SOURCE LINE 22
        __M_writer(escape(c.mydump))
        __M_writer(u' \')\';\n        var i;\n\tfor(i in mylist) {\n  \t\talert("mylist - " + mylist[i]);\n\t}\n\t//for (j = 0; j < ')
        # SOURCE LINE 27
        __M_writer(escape(c.plugincount))
        __M_writer(u'; j++)  {\n\t// \t% i.next()     \n\t//\talert ("hello ')
        # SOURCE LINE 29
        __M_writer(escape(i.next()))
        __M_writer(u'");\n\t//}\n</script>\n\n\n\n</head>\n\n\n<body>\n\n<div id="backwrap" class="bodybg">\n     <div id="menu_divider">\n     <div id="partners_gep_ab_logged">\n     <img src="http://')
        # SOURCE LINE 43
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\n     </div> <!-- right close-->\n\n\n\n\n\n     <ul id="nav" >\n                <li>  <a href="www.rediffmail.com">Home</a>   </li>\n                <li>  <a href="www.rediffmail.com">Intro Video</a>   </li>\n                <li>  <a href="www.rediffmail.com">How it works?</a>   </li>\n                <li>  <a href="www.rediffmail.com">Contact Us</a>  </li>\n\n     </ul>\n     </div>  <!-- menu divider close-->\n     </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


