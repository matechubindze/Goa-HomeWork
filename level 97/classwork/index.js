function countWords(sentence) {
    let trimmed = sentence.trim().replace(/\s+/g, " ");
    if (trimmed === "") return 0;
    return trimmed.split(" ").length;
}

console.log(countWords("   Hello   world   "));
console.log(countWords("This   is   a   test"));
console.log(countWords(""));


function allStrings(arr) {
  for (let el of arr) {
    if (typeof el !== "string") return false
  }
  return true
}

console.log(allStrings(["a","b","c"]))
console.log(allStrings(["a",2,"c"]))



function allActive(arr) {
  for (let el of arr) {
    if (el.status !== "active") return false
  }
  return true
}

console.log(allActive([{status:"active"},{status:"active"}]))  
console.log(allActive([{status:"active"},{status:"inactive"}]))
