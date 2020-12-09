var observer = new MutationObserver(function (mutations, me) {
    var elem = document.querySelector('#dash > div > div > div > div > div > form > div:nth-child(2) > div > dl > dd > div > textarea');
    elem.setAttribute('id', 'summernote');
    console.log(elem);
    var e = elem.id;
    for (let i=1; i >= e.length; i++){
        $('#' + e).summernote();
        }
    if (elem) {
        me.disconnect(); // stop observing
        return;
      }
});
// start observing
observer.observe(document, {
    childList: true,
    subtree: true
  });