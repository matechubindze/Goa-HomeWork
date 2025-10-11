function checkStringLength(str) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (str.length % 2 === 0) {
        resolve(str);
      } else {
        reject(str);
      }
    }, 2000);
  });
}

const promises = [
  checkStringLength("hello"),
  checkStringLength("worlds"),
  checkStringLength("test")
];

Promise.all(promises)
  .then(results => {
    console.log(results);
  })
  .catch(error => {
    console.log(error);
  });


const apiUrl = "https://goa-api.vercel.app/";

fetch(apiUrl)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));


fetch('https://fakestoreapi.com/products')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
