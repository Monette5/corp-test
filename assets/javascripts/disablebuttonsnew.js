function hideButton(button) {
  console.log("Button exists, hiding it");
  button.setAttribute('style', 'display:none');
}
window.onload = function() {

  var browseButton = document.querySelector('.nav li:nth-child(3)');
  var deployButton = document.querySelector('.btn-group button:nth-child(2)');
  if (browseButton !== null && deployButton !== null) {
    hideButton(browseButton);
    hideButton(deployButton);
    return true;
  }
    else {
      //setTimeout(function () {
      const myInterval = setInterval(myFunction, 500);
      function myFunction() {
          $(document).ready(function () {
            if (browseButton !== null && deployButton !== null) {
                hideButton(browseButton);
                hideButton(deployButton);
                  clearInterval(myInterval);
              }
          });
      }
  }
   
}
