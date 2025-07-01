var rates = [
    { currency: 'USD', buy: 2.65, sell: 2.70 },
    { currency: 'EUR', buy: 2.85, sell: 2.90 },
    { currency: 'GBP', buy: 3.30, sell: 3.40 }
];


var tableBody = document.querySelector("#rates-table tbody");

for (var i = 0; i < rates.length; i++) {
    var rate = rates[i];
    var row = document.createElement("tr");

    row.innerHTML =
    "<td>" + rate.currency + "</td>" +
    "<td>" + rate.buy.toFixed(2) + "</td>" +
    "<td>" + rate.sell.toFixed(2) + "</td>";

    tableBody.appendChild(row);
}

var updateDate = document.getElementById("update-date");
var now = new Date();
var formattedDate = now.toLocaleDateString("ka-GE", {
    year: "numeric",
    month: "long",
    day: "numeric"
});
updateDate.textContent = "განახლებულია: " + formattedDate;

// კონვერტაციის ფუნქცია
function convert() {
    var amount = parseFloat(document.getElementById("amount").value);
    var currency = document.getElementById("currency").value;
    var resultElement = document.getElementById("result");

    if (isNaN(amount) || amount <= 0) {
        resultElement.textContent = "გთხოვ შეიყვანე სწორი თანხა.";
        return;
    }

    var selectedRate = null;
    for (var j = 0; j < rates.length; j++) {
        if (rates[j].currency === currency) {
        selectedRate = rates[j];
        break;
    }
}

    if (!selectedRate) {
        resultElement.textContent = "ვალუტის კურსი ვერ მოიძებნა.";
        return;
    }

    var gel = amount * selectedRate.sell;
    resultElement.textContent = amount + " " + currency + " = " + gel.toFixed(2) + " ლარი (GEL)";
}