<<<<<<< HEAD
let alertBtn = document.getElementById("alertBtn")
let hoverText = document.getElementById("hoverText")
let toggleDiv = document.getElementById("toggleDiv")
let inputBox = document.getElementById("inputBox")
let toggleImageBtn = document.getElementById("toggleImageBtn")
let image = document.getElementById("image")

toggleDiv.style.width = "200px"
toggleDiv.style.height = "100px"
toggleDiv.style.backgroundColor = "lightblue"
toggleDiv.style.marginBottom = "20px"

image.style.width = "150px"
image.style.display = "block"
image.style.marginTop = "10px"

alertBtn.addEventListener("click", function() {
  alert("Button was clicked")
})

hoverText.addEventListener("mouseover", function() {
  hoverText.textContent = "Text has changed"
})

toggleDiv.addEventListener("click", function() {
  if (toggleDiv.style.backgroundColor === "lightblue") {
    toggleDiv.style.backgroundColor = "lightgreen"
  } else {
    toggleDiv.style.backgroundColor = "lightblue"
  }
})

inputBox.addEventListener("click", function() {
  console.log(inputBox.value)
})

toggleImageBtn.addEventListener("click", function() {
  if (image.style.display === "none") {
    image.style.display = "block"
  } else {
    image.style.display = "none"
  }
})
=======
let alertBtn = document.getElementById("alertBtn")
let hoverText = document.getElementById("hoverText")
let toggleDiv = document.getElementById("toggleDiv")
let inputBox = document.getElementById("inputBox")
let toggleImageBtn = document.getElementById("toggleImageBtn")
let image = document.getElementById("image")

toggleDiv.style.width = "200px"
toggleDiv.style.height = "100px"
toggleDiv.style.backgroundColor = "lightblue"
toggleDiv.style.marginBottom = "20px"

image.style.width = "150px"
image.style.display = "block"
image.style.marginTop = "10px"

alertBtn.addEventListener("click", function() {
  alert("Button was clicked")
})

hoverText.addEventListener("mouseover", function() {
  hoverText.textContent = "Text has changed"
})

toggleDiv.addEventListener("click", function() {
  if (toggleDiv.style.backgroundColor === "lightblue") {
    toggleDiv.style.backgroundColor = "lightgreen"
  } else {
    toggleDiv.style.backgroundColor = "lightblue"
  }
})

inputBox.addEventListener("click", function() {
  console.log(inputBox.value)
})

toggleImageBtn.addEventListener("click", function() {
  if (image.style.display === "none") {
    image.style.display = "block"
  } else {
    image.style.display = "none"
  }
})
>>>>>>> bc270391f93c5c2d2b9d8f76ce034f1c2fa5282d
