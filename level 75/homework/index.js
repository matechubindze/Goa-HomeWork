<<<<<<< HEAD
let i = 1;

let timer = setInterval(function() {
  console.log(i);
  i++;
  if (i > 5) {
    clearInterval(timer);
  }
}, 1000);
let a = 1;
let counter1 = setInterval(function() {
  console.log(a);
  a++;
  if (a > 5) {
    clearInterval(counter1);
  }
}, 1000);

let msg = setInterval(function() {
  console.log("This is a message");
}, 2000);
setTimeout(function() {
  clearInterval(msg);
}, 10000);

let change = 0;
let colors = ["red", "blue", "green", "yellow", "orange"];
let bg = setInterval(function() {
  document.body.style.backgroundColor = colors[change];
  change++;
  if (change >= 5) {
    clearInterval(bg);
  }
}, 3000);

let timeLog = setInterval(function() {
  console.log(new Date().toLocaleTimeString());
}, 1000);
setTimeout(function() {
  clearInterval(timeLog);
}, 15000);

let seconds = 0;
let timer2 = setInterval(function() {
  console.log(seconds);
  seconds++;
  if (seconds > 10) {
    clearInterval(timer);
  }
}, 1000);

let nums = [10, 20, 30, 40];
console.log(nums[1]);

nums[0] = 100;
console.log(nums);

let words = ["apple", "banana", "cherry"];
console.log(words[0]);
console.log(words[1]);
console.log(words[2]);

let values = [5, 10, 15, 20, 25];
let sum = values[0] + values[4];
console.log(sum);
=======
let i = 1;

let timer = setInterval(function() {
  console.log(i);
  i++;
  if (i > 5) {
    clearInterval(timer);
  }
}, 1000);
let a = 1;
let counter1 = setInterval(function() {
  console.log(a);
  a++;
  if (a > 5) {
    clearInterval(counter1);
  }
}, 1000);

let msg = setInterval(function() {
  console.log("This is a message");
}, 2000);
setTimeout(function() {
  clearInterval(msg);
}, 10000);

let change = 0;
let colors = ["red", "blue", "green", "yellow", "orange"];
let bg = setInterval(function() {
  document.body.style.backgroundColor = colors[change];
  change++;
  if (change >= 5) {
    clearInterval(bg);
  }
}, 3000);

let timeLog = setInterval(function() {
  console.log(new Date().toLocaleTimeString());
}, 1000);
setTimeout(function() {
  clearInterval(timeLog);
}, 15000);

let seconds = 0;
let timer2 = setInterval(function() {
  console.log(seconds);
  seconds++;
  if (seconds > 10) {
    clearInterval(timer);
  }
}, 1000);

let nums = [10, 20, 30, 40];
console.log(nums[1]);

nums[0] = 100;
console.log(nums);

let words = ["apple", "banana", "cherry"];
console.log(words[0]);
console.log(words[1]);
console.log(words[2]);

let values = [5, 10, 15, 20, 25];
let sum = values[0] + values[4];
console.log(sum);
>>>>>>> 8803ceab7c3d2c09642d327d76d2ac81c62a1822
