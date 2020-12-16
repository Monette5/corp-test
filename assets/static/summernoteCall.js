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
const markupStr = $('#summernote').summernote('code');
const editbtn = document.querySelector('.nav li:nth-child(1)');
var btn = $('.btn-primary');
$(btn).click(function () {

        const el = document.querySelector('textarea.form-control').innerHTML;
        const elm = $('note-editable card-block').summernote('code');
        $(elm).clone().appendTo(el);


});
});
$(document).ready(function () {
    const elem = document.querySelector('textarea.form-control');
    addSummer(elem);
});
function example(element) {
    if (window.location.href.indexOf(element) > -1) {
        return true;
    }
}





