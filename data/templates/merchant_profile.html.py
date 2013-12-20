# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332865824.463513
_template_filename='/home/purvi/Desktop/BE/project/padmaj/pylons/fiesta/fiesta/templates/merchant_profile.html'
_template_uri='/merchant_profile.html'
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
        __M_writer(u'<html>\r\n<head>\r\n<title>Fiesta: signupSuccess</title>\r\n<script src="http://')
        # SOURCE LINE 4
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/js/jquery.js"></script>\r\n<link rel="stylesheet" href="http://')
        # SOURCE LINE 5
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/css/main.css"media="screen" type="text/css"/>\r\n<script type="text/javascript">\r\n$(document).ready (function (){\r\n//alert("done");\r\n\r\nvar shops = new Array();\r\n\r\n//--------------------------------------------\r\n//alert("cid"+')
        # SOURCE LINE 13
        __M_writer(escape(c.id))
        __M_writer(u");\r\nvar url = 'http://")
        # SOURCE LINE 14
        __M_writer(escape(config['myhost']))
        __M_writer(u":5000/userauth/getshops?id='+")
        __M_writer(escape(c.id))
        __M_writer(u'+\'&callback=?\';\r\n//alert("before the call-"+url);\r\njQuery.getJSON(url, \r\n  function(data) {\r\n  //alert("Hello " + data.myshop);\r\n  shops = data.myshop;\r\n  //alert("shops " + shops[1]);\r\n  });\r\n\r\n//---------------------------------------------\r\n\r\nvar body = document.getElementById("dataTables_wrapper");\r\n        var tbl     = document.createElement("table");\r\n        var tblBody = document.createElement("tbody");\r\n\t\r\n           var row = document.createElement("tr");\r\n\r\n\t    var cell1 = row.insertCell(0);\r\n            cell1.innerHTML = "Sr. no";\r\n\r\n\t    var cell1 = row.insertCell(1);\r\n            cell1.innerHTML = "Online Store"\r\n\t\t\r\n\t    var cell1 = row.insertCell(2);\r\n            cell1.innerHTML = "Actions"\r\n\r\n            tblBody.appendChild(row);\r\n\t\trow.setAttribute("border-bottom" ,"1px solid #FFFFFF"); \r\n\t\trow.setAttribute("height","25px");\r\n\t\trow.setAttribute("bgcolor","#FFF8C6");\r\n\t\trow.setAttribute("font-weight","bold");\r\n         \trow.setAttribute("color","#7d5d41");\r\n\r\n\tvar x;\r\n\talert("Welcome!");\r\n\t//alert("shops are: "+ shops);\t\r\n        // creating all cells\r\n        for (x in shops) {\r\n            // creates a table row\r\n\t  //  alert("in loop " + x)\r\n            var row = document.createElement("tr");\r\n\r\n           var cell1 = row.insertCell(0);\r\n            cell1.innerHTML = parseInt(x)+1\r\n\r\n            var cell2 = row.insertCell(1);\r\n            cell2.innerHTML = shops[x];\r\n\t    url = "http://')
        # SOURCE LINE 61
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showshopinfo?fbid=')
        __M_writer(escape(c.id))
        __M_writer(u'&store="+shops[x]; \r\n \t    //alert("url is: "+url);\r\n \r\n            var cell3 = row.insertCell(2);\r\n\t   \r\n\t   // alert("url is "+ url)\r\n\t\r\n            cell3.innerHTML = \'<a href = \'+url+\'> view </a>\'\r\n\t\t\r\n                 \r\n\r\n            // add the row to the end of the table body\r\n            tblBody.appendChild(row);\r\n        }\r\n\r\n        // put the <tbody> in the <table>\r\n        tbl.appendChild(tblBody);\r\n        // appends <table> into <body>\r\n        body.appendChild(tbl);\r\n        // sets the border attribute of tbl to 2;\r\n        tbl.setAttribute("border-collapse","collapse");\r\n\ttbl.setAttribute("margin","0 auto");\r\n\ttbl.setAttribute("width","60%");\r\n\ttbl.setAttribute("border", "0");\r\n\ttbl.setAttribute("text-align", "center");\r\n});\r\n\r\n\r\n\r\nfunction loadshopinfo(url) {\r\n\talert("in loadshopinfo " + url)\r\n\tjQuery.get(url);\r\n\t//alert("Hit");\r\n}\r\n\r\n\r\n\r\n</script>\r\n</head>\r\n<body>\r\n<div id="backwrap" class="bodybg">\r\n\t\r\n\r\n<div id="partners_gep_ab_logged">\r\n\t<img src="http://')
        # SOURCE LINE 105
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/images/logo.png" height="90" width="250" border="0" hspace=150 />\r\n<div class="right">\r\n<a href=""  style="text-decoration:none; color: white" margin="10px 100px 0px"> Welcome ')
        # SOURCE LINE 107
        __M_writer(escape(c.name))
        __M_writer(u'</a>\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://')
        # SOURCE LINE 108
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/showprofile?doc_id=')
        __M_writer(escape(c.id))
        __M_writer(u'"  style="text-decoration:none; color: white"> Merchant Profile</a>\r\n\t&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.facebook.com/logout.php?next=http://')
        # SOURCE LINE 109
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html&access_token=')
        __M_writer(escape(config['accesstoken']))
        __M_writer(u'" style="text-decoration:none; color: white"> Logout </a>\r\n</div>\t \r\n\t   </div> <!-- right close-->\r\n\t<ul id="nav" class="tabs blue-tabs">\r\n<li><a href="http://')
        # SOURCE LINE 113
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html"> HOME</a>  </li>\r\n<li><a href="http://')
        # SOURCE LINE 114
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html"> Social Plugins</a>  </li>\r\n<li><a href="http://')
        # SOURCE LINE 115
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html"> About Us</a>  </li>\r\n<li><a href="http://')
        # SOURCE LINE 116
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html"> Contact Us</a>  </li>\r\n</ul>\r\n\r\n\t</div>  <!-- menu divider close-->\r\n\r\n  <div class= "highlights">\r\n    <div class ="hl_wrapper">\r\n      <div id="mainbody">\r\n\t<br/> <br/>\r\n        <div class="tab_header">\r\n          <div id= "tb-heading">Online Stores </div>\r\n        </div>\r\n  <div>\r\n<a href="http://')
        # SOURCE LINE 129
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/retailer/signup?name=')
        __M_writer(escape(c.name))
        __M_writer(u'&id=')
        __M_writer(escape(c.id))
        __M_writer(u'">\r\n          <button id="id_send_button" style="font-size: 16px; width: 200px; height: 35px; padding: 8px; font-weight: normal; color: #000000; background-color: #FFF8C6; margin: 40px 700px 10px" type="button" align="right">Add online Store</button></a>\r\n</div>\r\n        <div id="dataTables_wrapper"> \r\n\r\n\r\n</div>\r\n\r\n       \r\n\r\n      </div> <!--mainbody-->\r\n      <br>\r\n   </div> <!--hl wraper close-->\r\n   </div><!--highlights close-->\r\n  \r\n  <div class="sc_footer gep_bold">\r\n      <a href="http://')
        # SOURCE LINE 145
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/homepage.html">Home</a> |  \r\n        <a href="http://')
        # SOURCE LINE 146
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/socialplugin.html">Social Plugins</a> |  \r\n        <a href="http://')
        # SOURCE LINE 147
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/AboutUs.html">About Fiesta</a> |  \r\n        <a href="http://')
        # SOURCE LINE 148
        __M_writer(escape(config['myhost']))
        __M_writer(u':5000/contactus.html">Contact Us</a> | \r\n\r\n\t<br/ ><br/>    \r\n       <span class="gep_font10px">*Padmaj*</span>\r\n</div>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


