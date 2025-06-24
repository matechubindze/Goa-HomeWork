let myName = setInterval(printName, 10000)

function printName() {
  console.log('Mate Chubinidze')
}

let stop = document.getElementById('main-button')
stop.addEventListener('click', function() {
  clearInterval(myName)
})

const name = ["Hello",23,false,{name: "Mate"}[1,2,3,4,5]]
console.log(name)

function traverseArr(arr) {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i])
  }
}

traverseArr([1, 2, 3, 4])
traverseArr(['a', 'b', 'c'])
