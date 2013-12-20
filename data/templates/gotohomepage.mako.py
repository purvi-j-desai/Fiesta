# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1331403208.469302
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/gotohomepage.mako'
_template_uri='/gotohomepage.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<script language="javascript">\ntop.location.href=\'http://')
        # SOURCE LINE 2
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/offer.html';\n</script>\n\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


