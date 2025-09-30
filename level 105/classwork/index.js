function hasOwn(o, k) {
  return o.hasOwnProperty(k);
}

let obj1 = {a: 1, b: 2};
let obj2 = {x: 10};
let obj3 = {name: "Nika"};

console.log(hasOwn(obj1, "a"));       
console.log(hasOwn(obj2, "y"));       
console.log(hasOwn(obj3, "toString"));