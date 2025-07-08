let total = 0;
do {
    let input = prompt("Enter a number:");
    total += Number(input);
} while (total <= 100);
alert("Total exceeded 100. Final total: " + total);


let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
}

let list = document.getElementById("myList")

for (let key in myObj) {
    let li1 = document.createElement("li")
    li1.textContent = key
    list.appendChild(li1)

    let li2 = document.createElement("li")
    li2.textContent = myObj[key]
    list.appendChild(li2)
}


let myArray = ["hello", "world", 5, 20, true, false];

for (let item of myArray) {
    if (typeof item === "string") {
        console.log(item);
    } else if (typeof item === "number") {
        console.log(item + 10);
    } else if (typeof item === "boolean") {
        console.log(!item);
    }
}
