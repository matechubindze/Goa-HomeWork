//Number 1
let number = parseFloat(prompt("Enter a number:"));

if (number > 0) {
  alert("The number is positive.");
} else if (number < 0) {
  alert("The number is negative.");
} else {
  alert("The number is zero.");
}
//Number 2
let age = parseInt(prompt("Enter your age:"));

if (age >= 18) {
  alert("You can vote!");
} else {
  alert("You are not eligible to vote.");
}
//Number 3
let num1 = parseFloat(prompt("Enter the first number:"));
let num2 = parseFloat(prompt("Enter the second number:"));

if (num1 > num2) {
  alert("The first number is larger.");
} else if (num2 > num1) {
  alert("The second number is larger.");
} else {
  alert("Both numbers are equal.");
}
