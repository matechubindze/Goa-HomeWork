function flipCoin() {
    let coin = Math.random() < 0.5 ? "არიოლი" : "რეშკა"
    document.getElementById("result").innerText = coin
    if (coin === "რეშკა") {
        document.body.style.background = "green"
    } else {
        document.body.style.background = "lightgray"
    }
}

function updateDateTime() {
    let now = new Date()
    let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
    document.getElementById("dateTime").innerText = now.toLocaleDateString("ka-GE", options) 
        + " " + now.toLocaleTimeString()
    document.getElementById("randomNum").innerText = Math.floor(Math.random() * 100)
}

setInterval(updateDateTime, 1000)
updateDateTime()
