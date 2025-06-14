<<<<<<< HEAD
let fruits = ["apple", "banana", "cherry", "mango", "orange"];
console.log(fruits[0]);
console.log(fruits[fruits.length - 1]);
console.log(fruits.length);

let colors = ["red", "green", "blue"];
colors.push("yellow");
colors.shift();
colors.unshift("purple");
console.log(colors);

let numbers = [2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}

function sumArray(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
console.log(sumArray([1, 2, 3]));

let decimal = parseFloat(prompt("Enter a decimal number:"));
console.log(Math.floor(decimal));
console.log(Math.ceil(decimal));
console.log(Math.round(decimal));

let nums = [10, 25, 3, 56, 7];
console.log(Math.max(...nums));
console.log(Math.min(...nums));

function findMax(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
  }
  return max;
}
console.log(findMax([12, 45, 3, 67, 22]));

let favoriteMovies = ["Inception", "Titanic", "Interstellar", "Avatar", "The Matrix"];
let movie = prompt("Enter a movie name:");
if (favoriteMovies.includes(movie)) {
  console.log("Yes, it's one of my favorites!");
} else {
  console.log("No, I don't like that one much.");
}

let words = ["banana", "apple", "pear", "orange"];
words.sort();
console.log(words.join(", "));

function randomOneToTen() {
  return Math.floor(Math.random() * 10) + 1;
}
console.log(randomOneToTen());
=======
let fruits = ["apple", "banana", "cherry", "mango", "orange"];
console.log(fruits[0]);
console.log(fruits[fruits.length - 1]);
console.log(fruits.length);

let colors = ["red", "green", "blue"];
colors.push("yellow");
colors.shift();
colors.unshift("purple");
console.log(colors);

let numbers = [2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}

function sumArray(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
console.log(sumArray([1, 2, 3]));

let decimal = parseFloat(prompt("Enter a decimal number:"));
console.log(Math.floor(decimal));
console.log(Math.ceil(decimal));
console.log(Math.round(decimal));

let nums = [10, 25, 3, 56, 7];
console.log(Math.max(...nums));
console.log(Math.min(...nums));

function findMax(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
  }
  return max;
}
console.log(findMax([12, 45, 3, 67, 22]));

let favoriteMovies = ["Inception", "Titanic", "Interstellar", "Avatar", "The Matrix"];
let movie = prompt("Enter a movie name:");
if (favoriteMovies.includes(movie)) {
  console.log("Yes, it's one of my favorites!");
} else {
  console.log("No, I don't like that one much.");
}

let words = ["banana", "apple", "pear", "orange"];
words.sort();
console.log(words.join(", "));

function randomOneToTen() {
  return Math.floor(Math.random() * 10) + 1;
}
console.log(randomOneToTen());
>>>>>>> 39956a2665078fbb72a118a0c590fce9b4264135
