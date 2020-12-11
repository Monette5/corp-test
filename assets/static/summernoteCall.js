function addElement (el) { 
const elem = document.querySelector('textarea.form-control');
    // create a new div element 
const newDiv = document.createElement("div"); 
newDiv.id = "summernote";
el.appendChild(newDiv);
}
//*[@id="dash"]/div/div/div/div/div/form/div[2]/div/dl/dd

// create an observer instance
  function log(mutations) {
    for (let mutation of mutations) {
        if (mutation.type === 'childList') {
            console.log(mutation);
        }
    }
}
let observer = new MutationObserver(log);
// onload = function() {
//     observer.observe(elem, {
//         childList: true
//     });

// }
    $(document).ready(function() {
    const elem = document.querySelector('textarea.form-control');
        // create a new div element 
    //const newDiv = document.createElement("div"); 
   // newDiv.id = "summernote";
   // elem.appendChild(newDiv);
   elem.id = "summernote";
    $("#summernote").removeClass('display', 'none');
    $("#summernote").addClass('display', 'block');
    $('#summernote').summernote({
        placeholder: 'Hello Bootstrap 4',
        tabsize: 2,
        height: 100
      });  
    });
// later, you can stop observing
observer.disconnect();






