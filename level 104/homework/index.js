class Teacher{
    constructor(name,subject){
        this.name = "Mate"
        this.subject = "English"
    }
    introduce(){
        "Hello,I am" + this.name + "and i teach" + this.subject;
    }
}


class Phone{
    constructor(Brand,Model){
        this.Brand = "mercedes"
        this.Model = "c63"
    }
    ring(){
        "The" + this.brand + this.Model + "is ringing"
    }
}

class Movie{
    constructor(title,year){
        this.title = "GOA"
        this.year = "2025"
    }
    play(){
        "Now playing" + this.title + (this.year);
    }

}

class Cat{
    constructor(name,color){
        this.name = "ჩორნა"
        this.color = "black"
    }
    meow(){
        this.name + "the" + this.color + "cat says meow"
    }
}

class BankCard{
    constructor(cardNumber,balance){
        this.cardNumber = 8239921
        this.balance = 1000
    }
    widthraw(amount){
        this.balance = this.balance - amount
    }
}
let user1 = new Bank("Mate")
user1.widthraw(200)
