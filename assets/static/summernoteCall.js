const markupStr = $('#summernote').summernote('code');
const editbtn = document.querySelector('.nav li:nth-child(1)');
function addSummer(elem) {
    elem.id = "summernote";
    $("#summernote").removeClass('display', 'none');
    $("#summernote").addClass('display', 'block');
    $('#summernote').summernote({
        placeholder: 'Hello Bootstrap 4',
        tabsize: 2,
        height: 100
    });
}

/* this.transitionToAdminPage('.preview', {
    path: this.getUrlRecordPathWithAlt(path) */
$(editbtn).click(function () {
    $(document).ready(function () {
        const elem = document.querySelector('textarea.form-control');
        if (elem !== null) {
            addSummer(elem);
        }
        else {
            //setTimeout(function () {
            const myInterval = setInterval(myFunction, 500);
            function myFunction() {
                $(document).ready(function () {
                    const elem = document.querySelector('textarea.form-control');
                    addSummer(elem);
                    if (elem !== null) {
                        clearInterval(myInterval);
                    }
                });
            }
        }
    });
});

$(document).ready(function () {
    const elem = document.querySelector('textarea.form-control');
    addSummer(elem);
});
/* $(document).ready(function () {;
    addElement();
}); */
function example(element) {
    if (window.location.href.indexOf(element) > -1) {
        return true;
    }
}
 




