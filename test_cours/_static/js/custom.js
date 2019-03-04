document.addEventListener("DOMContentLoaded", function(event) {
  Array.prototype.slice.call(document.querySelectorAll('.blq'))
    .forEach(function(elem) {
      elem.onclick = function () {
        if (this.classList.contains('spoiler')) {
        this.classList.remove('spoiler');
      } else {
        this.classList.add('spoiler');
      }
    };
  });
});
