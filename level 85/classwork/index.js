function printEvenNumbers() {
  for (let num of arguments) {
    if (num % 2 === 0) {
      console.log(num)
    }
  }
}

printEvenNumbers(11, 22, 33, 44, 55, 66, 77, 88, 99, 100)

//არ არის ანონიმური
const myFunc = function(){
    console.log("Hello World!!!!")
}
//არის ანონიმური
const func = () => {
    console.log("helo world!!")
}
//(ორივე ანონიმურია)

console.log((function(){
    return "hello world!!"
})())

let message = "Hello"; // global scope

function helloWorld() {
  let word = "World"; // function scope

  if (true) {
    let symbol = "!"; // block scope
    console.log(symbol);
  }

  console.log(word);
}

helloWorld();
console.log(message);
