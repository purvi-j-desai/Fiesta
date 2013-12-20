# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1331402887.168169
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/saltation.mako'
_template_uri='/saltation.mako'
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
        __M_writer(u'<script language="javascript">\ntop.location.href=\'https://www.facebook.com/dialog/feed?app_id=')
        # SOURCE LINE 2
        __M_writer(escape(config['facebook.appid']))
        __M_writer(u'&link=https://developers.facebook.com/docs/reference/dialogs/&picture=http://fbrell.com/f8.jpg&name=Facebook%20Dialogs&caption=Reference%20Documentation&%20description=Using%20Dialogs%20to%20interact%20with%20users.&message=Facebook%20Dialogs%20are%20so%20easy!&%20redirect_uri=http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/offer.html&display=popup'\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


