let allParagraphs = document.getElementsByTagName("p")
let texts = []
for (let i = 0; i < allParagraphs.length; i++) {
  texts.push(allParagraphs[i].textContent)
}
console.log(texts)


let container = document.getElementById("container")
for (let i = 1; i <= 5; i++) {
  let p = document.createElement("p")
  p.textContent = "This is paragraph number " + i
  container.appendChild(p)
}

const div = document.getElementById("myDiv")
const paragraphs = div.getElementsByTagName("p")

for (let i = 0; i < paragraphs.length; i++) {
  paragraphs[i].style.color = "green"
  paragraphs[i].style.backgroundColor = "black"
}

