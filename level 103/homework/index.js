setInterval(() => {
    let now = new Date()
    console.log(now.toLocaleString())
}, 1000)

let dice = Math.floor(Math.random() * 6) + 1
console.log(dice)

let fruits = ["ვაშლი", "მსხალი", "ბანანი", "ატამი"]
let randomFruit = fruits[Math.floor(Math.random() * fruits.length)]
console.log(randomFruit)

let chars = "goa"
let password = ""
for (let i = 0; i < 8; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length))
}
console.log(password)

let months = ["იანვარი","თებერვალი","მარტი","აპრილი","მაისი","ივნისი","ივლისი","აგვისტო","სექტემბერი","ოქტომბერი","ნოემბერი","დეკემბერი"]
let m = new Date().getMonth()
console.log(months[m])

let days = ["კვირა","ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი"]
let d = new Date().getDay()
console.log(days[d])

function birthdayCountdown(month, day) {
    let now = new Date()
    let year = now.getFullYear()
    let next = new Date(year, month - 1, day)
    if (next < now) next = new Date(year + 1, month - 1, day)
    let diff = Math.ceil((next - now) / (1000 * 60 * 60 * 24))
    console.log(diff)
}
birthdayCountdown(12, 25)

let start
function startTimer() {
    start = Date.now()
}
function stopTimer() {
    let seconds = (Date.now() - start) / 1000
    console.log(seconds)
}

let r = Math.floor(Math.random() * 256)
let g = Math.floor(Math.random() * 256)
let b = Math.floor(Math.random() * 256)
console.log("rgb(" + r + "," + g + "," + b + ")")
