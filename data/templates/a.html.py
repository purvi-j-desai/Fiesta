# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1327892135.315711
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/a.html'
_template_uri='/a.html'
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
        __M_writer(u'<html>\n<head>\n<script language = javascript>\n $user_id = ')
        # SOURCE LINE 4
        __M_writer(escape(c.id))
        __M_writer(u' \n alert("logged in user = " + $user_id)\n</script> \n</head>\n<body>\n\t\n\t\n<h1>Merchant signup page</h1>\t\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


