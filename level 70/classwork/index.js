function userLoop() {
  let num1 = Number(prompt("Enter the first number:"))
  let num2 = Number(prompt("Enter the second number:"))
  for (let i = num1; i <= num2; i++) {
    console.log(i)
  }
}

userLoop()

function changeElements() {
  const input = document.getElementById("myInput");
  const button = document.getElementById("myButton");
  const title = document.getElementById("title");

  console.log(input.value);
  button.style.backgroundColor = "black";
  button.style.color = "white";
  title.style.textAlign = "center";
  document.body.style.backgroundColor = "green";
}
