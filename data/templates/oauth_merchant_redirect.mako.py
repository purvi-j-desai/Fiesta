# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332891758.609019
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/oauth_merchant_redirect.mako'
_template_uri='/oauth_merchant_redirect.mako'
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
        __M_writer(u'<script language="javascript">\n\ntop.location.href=\'https://www.facebook.com/dialog/oauth?client_id=')
        # SOURCE LINE 3
        __M_writer(escape(config['facebook.appid']))
        __M_writer(u'&redirect_uri=http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/userauth/authnext&display=popup&scope=email'\n\n</script>\n\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


