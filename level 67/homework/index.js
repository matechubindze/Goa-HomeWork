let emptyObj = {};

let person = { name: "Alex", age: 30, city: "New York" };

let personName = person.name;

person.country = "USA";

let user = {
  id: 1,
  profile: {
    username: "alex123",
    email: "alex@example.com"
  }
};

person.age = 31;

let a = 15;
let b = 20;
let bothGreaterThan10 = a > 10 && b > 10;

let atLeastOneTrue = a > 10 || b < 10;

let isAvailable = true;
let notAvailable = !isAvailable;

let complexCondition = (a > 10 && b > 10) || !isAvailable;

let num = 123;
let numStr = String(num);

let bool = false;
let boolStr = String(bool);

let strNum = "456";
let convertedNum = Number(strNum);

let trueNum = Number(true);
let falseNum = Number(false);

let invalidConversion = Number("hello");
