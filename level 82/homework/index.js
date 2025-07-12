 for (let i = 0; i<=20; i++){
     if(i ===13){
         break
     }
     console.log(i)
 }

let colors = ["red", "green", "yellow", "blue", "purple"];

for (let color of colors) {
    if (color === "blue") {
        break;
    }
    console.log(color);
}
for (i = 1;i <= 50;i++){
    if (i % 4 === 0 && i % 5 === 0){
        break
    }
    console.log(i)
}
for (let i = 1; i <= 20; i++) {
    if (i === 13) continue;
    console.log(i);
}

let fruits = ["apple", "banana", "orange", "grape"];
for (let fruit of fruits) {
    if (fruit === "banana") continue;
    console.log(fruit);
}

for (let i = 1; i <= 30; i++) {
    if (i % 3 === 0) continue;
    console.log(i);
}

let word = "developer";

for (let letter of word) {
    if (letter === "e") continue;
    console.log(letter);
}

for (let i = 1; i <= 50; i++) {
    if (i % 2 === 0) continue;
    console.log(i);
}

let add = (a, b) => a + b;

let greet = name => "Hello, " + name + "!";

let doubleArray = arr => arr.map(x => x * 2);

let isEven = n => n % 2 === 0;

let strLength = str => str.length;
