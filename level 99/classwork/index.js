let products = [
  {name: "Book", price: 50},
  {name: "Phone", price: 200},
  {name: "Pen", price: 20}
]

let cheap = products.filter(p => p.price < 100)

console.log(cheap)


const elemnetsArr1 = ["hello","GOA","world","ball"]

console.log(elemnetsArr1.find(word => word.startsWith("b")))

const myArr1 = [1,2,3,4,5,]

console.log(myArr1.splice(2,0,99))