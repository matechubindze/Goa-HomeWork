//საკლასო დავალება:

// html-ის სტრუქტურაში ჩაამატეთ ერთი დივ ბლოკი და მას გაუწერეთ id.

// js-ში შექმენით ფუნქცია სახელად addNewElement. ამ ფუნქციაში ჯერ წამოიღეთ დივ ბლოკი, შემდეგ შექმენით ღილაკი. ღილაკს გაუწერეთ თავისი ტექსტი - გამოიყენეთ პირდაპირ textContent ან createTextNode და appendChild მეთოდები. საბოლოოდ ღილაკი ჩაამატეთ დივ ბლოკში. 

// ამ დავალებისთვის დაგჭირდებათ შემდეგი მეთოდები და კუთვნილებები: getElementById, textContent, createTextNode, appendChild
function addNewElement(){
    let div = document.getElementById("main-div")
    let button = document.createElement("button")
    button.textContent = "click Me"
    div.appendChild(button)

}