# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1329452488.983445
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/showshopinfo.html'
_template_uri='/showshopinfo.html'
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
        __M_writer(u'<html>\n<head>\n<title> Fiesta : Merchant Profile</title>\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/> \n\n<script src="http://')
        # SOURCE LINE 7
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/all.js"></script>\n<style type="text/css">\n\n#labelf {font-family : garamond, times; font-size: 10px }\n</style>\n\n</head>\n<body>\n\n<h1>Shop details:</h1>\n\n<h2>Partner ID : ')
        # SOURCE LINE 18
        __M_writer(escape(c.doc_id))
        __M_writer(u'</h2>\n<h2>Store : ')
        # SOURCE LINE 19
        __M_writer(escape(c.store_name))
        __M_writer(u'</h2>\n<h2>URL : ')
        # SOURCE LINE 20
        __M_writer(escape(c.site_url))
        __M_writer(u'</h2>\n\n\n\n\n<div class="sc_footer gep_bold">\n\n\n    \n        <a href="www.rediffmail.com">Home</a> |  \n        <a href="www.rediffmail.com">Intro Video</a> |  \n        <a href="www.rediffmail.com">How it works?</a> |  \n        <a href="www.rediffmail.com">Contact Us</a> | \n\n\t<br/ ><br/>\n    \n       <span class="gep_font10px">*Padmaj*</span>\n    \n\n\n\n</div>\n\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


