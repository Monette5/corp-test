$(document).ready(function() {
    var elem = $('#dash textarea');
    var newdiv1 = $( "<div id='summernote'></div>" );
    elem.append(newdiv1);
    $("#summernote").summernote();
});


