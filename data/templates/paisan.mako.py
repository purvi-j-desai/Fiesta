# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1329760371.171237
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/paisan.mako'
_template_uri='/paisan.mako'
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
        __M_writer(u'<script language="javascript">\ntop.location.href=\'https://www.facebook.com/plugins/like.php?href=')
        # SOURCE LINE 2
        __M_writer(escape(c.siteurl))
        __M_writer(u"&amp;layout=standard&amp;show_faces=true&amp;width=450&amp;action=like&amp;colorscheme=light&display=popup'\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


