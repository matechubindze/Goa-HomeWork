const filterPositive = (arr) => {
  for (let num of arr) {
    if (num < 0) continue;
    console.log(num);
  }
};

const findLongWord = (words) => {
  for (let word of words) {
    if (word.length > 5) {
      console.log(word);
      break;
    }
  }
};

const sumUntilNegative = (nums) => {
  let sum = 0;
  for (let num of nums) {
    if (num < 0) break;
    sum += num;
  }
  console.log(sum);
};

const skipMultiplesOf3 = () => {
  for (let i = 1; i <= 20; i++) {
    if (i % 3 === 0) continue;
    console.log(i);
  }
};

const countWordsWithA = (words) => {
  let count = 0;
  for (let word of words) {
    if (word.length < 1) continue;
    if (word[0] === "A" || word[0] === "a") count++;
  }
  console.log(count);
};

const skip4and6Multiples = () => {
  for (let i = 1; i <= 30; i++) {
    if (i % 4 === 0 || i % 6 === 0) continue;
    console.log(i);
  }
};

const findLongName = (names) => {
  for (let name of names) {
    if (name.length > 8) {
      console.log(name);
      break;
    }
  }
};

const printOddNumbers = (arr) => {
  for (let num of arr) {
    if (num % 2 === 0) continue;
    console.log(num);
  }
};

const sumPositiveEven = (arr) => {
  let sum = 0;
  for (let num of arr) {
    if (num <= 0 || num % 2 !== 0) continue;
    sum += num;
  }
  console.log(sum);
};
