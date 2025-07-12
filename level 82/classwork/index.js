function sumNumbers() {
    let sum = 0;
    let i = 0;
    while (i <= 10) {
        if (i % 2 !== 0) {
            i++;
            continue;
        }
        sum += i;
        i++;
    }
    console.log(sum);
}

sumNumbers();


let day = 3;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
  default:
    console.log("Invalid day");
}

const isEven = number => {
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
};
