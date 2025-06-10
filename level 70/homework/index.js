for (let i = 1; i <= 10; i++) {
  console.log(i);
}
let i = 2
while(i <= 20){
    console.log(i)
    i = i + 2
}
for(let i = 10;i >= 1;i--){
    console.log(i)
}
let i2 = 1;
while (i <= 5) {
  console.log(i2 * 3);
  i++;
}
const str = "Hello"
for (let i = 0; i < str.length; i++) {
  console.log(str[i])
}

const colorDiv = document.getElementById('colorDiv')
colorDiv.style.width = '100px'
colorDiv.style.height = '100px'
colorDiv.style.backgroundColor = 'lightgray'

const hideDiv = document.getElementById('hideDiv')
hideDiv.style.width = '100px'
hideDiv.style.height = '100px'
hideDiv.style.backgroundColor = 'lightblue'
hideDiv.style.marginTop = '10px'

document.getElementById('changeTextBtn').onclick = function() {
  document.getElementById('textPara').textContent = 'Text Changed'
}

document.getElementById('changeColorBtn').onclick = function() {
  colorDiv.style.backgroundColor = 'orange'
}

document.getElementById('changeFontBtn').onclick = function() {
  document.getElementById('heading').style.fontSize = '40px'
}

document.getElementById('hideDivBtn').onclick = function() {
  hideDiv.style.display = 'none'
}

