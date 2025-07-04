let paragraphs = document.getElementsByTagName("p")
alert("the number of p tags are: " + paragraphs.length);

let h2Div = document.getElementById("h2-div")
h2Div.style.backgroundColor = "blue"

let divBlocks = document.getElementById("div-div")
divBlocks.style.backgroundColor = "lightgray"

let paragraphs2 = document.getElementsByClassName("card")
console.log("the number of classes named card are: " + paragraphs2.length)

let paragraphs3 = document.getElementsByClassName("error")

for (i = 0;i < paragraphs3.length; i++){
    paragraphs3[i].style.backgroundColor = "red"
}
let buttons = document.getElementsByClassName("button")

for (i = 0;i < buttons.length; i++){
    buttons[i].textContent = "clicked";
}
let div2 = document.getElementById("animation-div")

let inertval = setInterval(function(){
    div2.style.marginLeft = "5px"
}, 100)
