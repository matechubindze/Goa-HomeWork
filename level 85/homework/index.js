function printArgs() {
  for (let arg of arguments) {
    console.log(arg)
  }
}

function countArgs() {
  console.log(arguments.length)
}

function sumNumbers() {
  let sum = 0
  for (let arg of arguments) {
    if (typeof arg === "number") {
      sum += arg
    }
  }
  console.log(sum)
}

function printUntilZero() {
  for (let arg of arguments) {
    if (arg === 0) break
    console.log(arg)
  }
}

function printOnlyNumbers() {
  for (let arg of arguments) {
    if (typeof arg === "string") continue
    console.log(arg)
  }
}

let multiply = function(a, b) {
  return a * b
}

setInterval(function() {
  console.log("running")
}, 2000)

document.querySelector("button").addEventListener("click", function() {
  alert("clicked")
})

(function() {
  console.log("Hello, world!")
})()

(function(num) {
  console.log(num * num)
})(5)

(function(arr) {
  let total = 0
  for (let n of arr) total += n
  console.log(total)
})([2, 4, 6])

function localVarExample() {
  let x = 10
}
try {
  console.log(x)
} catch (e) {
  console.log("error")
}

function outer() {
  let value = 1
  function inner() {
    value += 5
  }
  console.log(value)
  inner()
  console.log(value)
}
outer()

function scopeTest() {
  if (true) {
    var a = 1
    let b = 2
    const c = 3
  }
  console.log(a)
  try {
    console.log(b)
  } catch (e) {
    console.log("error")
  }
  try {
    console.log(c)
  } catch (e) {
    console.log("error")
  }
}
scopeTest()
