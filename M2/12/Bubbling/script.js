var form = document.querySelector('form');

var elems = document.querySelectorAll('form,div,p');

for (var i = 0; i < elems.length; i++) {
  elems[i].addEventListener("click", highlightThis, true);
}
function highlightThis(event) {
  event.target.style.backgroundColor = 'yellow';
  alert("target = " + event.target.tagName + ", this=" + this.tagName);
  event.target.style.backgroundColor = '';
};