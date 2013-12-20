# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332879901.893673
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/oauth_user_redirect.mako'
_template_uri='/oauth_user_redirect.mako'
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
        __M_writer(u'<script language="javascript">\ntop.location.href=\'https://www.facebook.com/dialog/oauth?client_id=')
        # SOURCE LINE 2
        __M_writer(escape(config['facebook.appid']))
        __M_writer(u'&redirect_uri=http://')
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/userauth/authnext&scope=email,publish_stream,user_birthday,user_relationships,user_relationship_details,friends_interests,friends_birthday,user_location,offline_access&display=popup';\n</script>\n\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


