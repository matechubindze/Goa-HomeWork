<<<<<<< HEAD
let i = 1;
do {
    console.log(i);
    i++;
} while (i <= 5);

let j = 2;
do {
    console.log(j);
    j += 2;
} while (j <= 10);

let k = 10;
do {
    console.log(k);
    k--;
} while (k >= 1);

let num;
do {
    num = parseInt(prompt("Enter number > 100"));
} while (num <= 100);

let sum = 0;
let x = 1;
do {
    sum += x;
    x++;
} while (x <= 10);
console.log(sum);

let arr = [1, 2, 3, 4, 5];
for (let el of arr) {
    console.log(el);
}

let text = "Hello";
for (let ch of text) {
    console.log(ch);
}

let arr2 = [10, 20, 30];
let total = 0;
for (let val of arr2) {
    total += val;
}
console.log(total);

let arr3 = [3, 4, 7, 8, 10];
for (let n of arr3) {
    if (n % 2 === 0) {
        console.log(n);
    }
}

let names = ["Ana", "Luka", "Nino", "Dato"];
for (let name of names) {
    console.log(name);
}

let obj = {
    name: "David",
    age: 25,
    city: "Tbilisi"
};

for (let key in obj) {
    console.log(key);
}

for (let key in obj) {
    console.log(obj[key]);
}

let count = 0;
for (let key in obj) {
    count++;
}
console.log(count);

let exists = false;
for (let key in obj) {
    if (key === "age") {
        exists = true;
    }
}
console.log(exists);

let keysString = "";
for (let key in obj) {
    keysString += key + " ";
}
console.log(keysString.trim());
=======
let i = 1;
do {
    console.log(i);
    i++;
} while (i <= 5);

let j = 2;
do {
    console.log(j);
    j += 2;
} while (j <= 10);

let k = 10;
do {
    console.log(k);
    k--;
} while (k >= 1);

let num;
do {
    num = parseInt(prompt("Enter number > 100"));
} while (num <= 100);

let sum = 0;
let x = 1;
do {
    sum += x;
    x++;
} while (x <= 10);
console.log(sum);

let arr = [1, 2, 3, 4, 5];
for (let el of arr) {
    console.log(el);
}

let text = "Hello";
for (let ch of text) {
    console.log(ch);
}

let arr2 = [10, 20, 30];
let total = 0;
for (let val of arr2) {
    total += val;
}
console.log(total);

let arr3 = [3, 4, 7, 8, 10];
for (let n of arr3) {
    if (n % 2 === 0) {
        console.log(n);
    }
}

let names = ["Ana", "Luka", "Nino", "Dato"];
for (let name of names) {
    console.log(name);
}

let obj = {
    name: "David",
    age: 25,
    city: "Tbilisi"
};

for (let key in obj) {
    console.log(key);
}

for (let key in obj) {
    console.log(obj[key]);
}

let count = 0;
for (let key in obj) {
    count++;
}
console.log(count);

let exists = false;
for (let key in obj) {
    if (key === "age") {
        exists = true;
    }
}
console.log(exists);

let keysString = "";
for (let key in obj) {
    keysString += key + " ";
}
console.log(keysString.trim());
>>>>>>> 6bac19caadae7bcc8764074c0e693ea66cfd98e6
