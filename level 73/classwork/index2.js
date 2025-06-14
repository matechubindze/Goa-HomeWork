function updateDiv() {
  let div = document.getElementById("myDiv");
  let button = document.getElementById("myButton");
  let para = document.getElementById("myPara");

  div.removeChild(button);

  let italic = document.createElement("i");
  italic.innerText = "This is the new italic text.";
  div.replaceChild(italic, para);
}

updateDiv();

