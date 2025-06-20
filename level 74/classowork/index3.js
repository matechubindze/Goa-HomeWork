let link = document.getElementById("myLink");

link.addEventListener("pointerover", function(e) {
  let attributes = e.target.attributes;

  for (let i = 0; i < attributes.length; i++) {
    console.log(attributes[i].name + ": " + attributes[i].value);
  }

  console.log(e.target);
});
