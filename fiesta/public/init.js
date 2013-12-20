function init(doc_id) {
    var url = 'http://localhost:5000/plugins/geturl?doc_id='+doc_id+'&callback=?';
    alert("before call-"+url);
    jQuery.getJSON(url, 
    function(data) {
	alert("data is : " + data);
    	alert("nexturl: " + data.nexturl);
	document.getElementById('fiesta_frame').src= data.nexturl;
    })
}


