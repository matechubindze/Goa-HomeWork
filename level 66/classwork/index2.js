const form = document.getElementById('myForm');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  const inputValue = form.elements['username'].value;
  alert(inputValue);
});
