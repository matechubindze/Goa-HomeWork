class Bank {
  constructor(username) {
    this.username = username
    this.balance = 0
  }

  deposit(amount) {
    this.balance = this.balance + amount
  }
}

let user1 = new Bank("Mate")
user1.deposit(100)
console.log(user1.username, user1.balance)



class Car{
    constructor(brand,model){
        this.brand = brand
        this.model = model 
    }
    start(){
        console.log(this.brand + " " + this.model + "is running")
    }
}
const cars = new car("Mercedes","BMW") 
cars.start()