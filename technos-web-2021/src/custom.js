const elems = document.querySelectorAll('span.tryit + a');
elems.forEach((item) => {
  item.setAttribute('target', 'blank');
  item.parentElement.classList.add('tryit-section');
  item.innerHTML = item.innerHTML.replace('http://mthh.pythonanywhere.com', '<span class="normal-before-bold">http://mthh.pythonanywhere.com</span>')
});
