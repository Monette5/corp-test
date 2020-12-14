const markupStr = $('#summernote').summernote('code');
const savebtn = document.querySelector('button.btn.btn-primary');
const editbtn = document.querySelector('.nav li:nth-child(1)');
function save() {
    $(savebtn).click(function () {
        $('textarea.form-control').text(markupStr);
        alert('saved');
    });
}
//
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
$(document).ready(function () {
    const elem = document.querySelector('textarea.form-control');
    addSummer(elem);
});

function example(element) {
    if (window.location.href.indexOf(element) > -1) {
        return true;
    }
}
//@TODO Loop the button group and set the textarea for each page selected and
// find a better way to wait for the edit page to be loaded
$(editbtn).click(function () {
    if (!example('edit')) {
        setTimeout(function () {
            const elem = document.querySelector('textarea.form-control');
            addSummer(elem);
        }, 5000);
    } else if (example('edit')) {
        $(document).ready(function () {
            const elem = document.querySelector('textarea.form-control');
            addSummer(elem);
        });
    }

});

$(savebtn).click(function () {
    save();
});












