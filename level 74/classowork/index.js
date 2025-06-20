// საკლასო დავალება:

// html-ის სტრუქტურაში დაამატეთ ერთი პარაგრაფი და მას გაუწერეთ id.

// js-ში წამოიღეთ ეს პარაგრაფი და მას გაუწერეთ onmouseover event handler. ამ event handler-ს გადაეცით ფუნქცია, რომელიც ვებსაიტზე ტექსტს განალაგებს ცენტრში
let p = document.getElementById("p1")
p.onmouseover = function(){
    p.style.alignItems = "center"
}