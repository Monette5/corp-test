const elem = document.querySelector('textarea.form-control');
//var newdiv1 = $("<div id='summernote'></div>");
elem.id = 'summernote';
// create an observer instance
  function log(mutations) {
    for (let mutation of mutations) {
        if (mutation.type === 'childList') {
            console.log(mutation);
        }
    }
}
let observer = new MutationObserver(log);
onload = function() {
    observer.observe(elem, {
        childList: true
    });

    $('#summernote').summernote();     
}
 
// later, you can stop observing
observer.disconnect();






