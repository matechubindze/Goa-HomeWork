function coinFlip() {
  return new Promise((resolve, reject) => {
    const result = Math.random() < 0.5 ? 'Heads' : 'Tails';

    if (result === 'Heads') {
      resolve('Heads');
    } else {
      reject('Tails');
    }
  });
}

coinFlip()
  .then(result => {
    console.log('Result:', result);
  })
  .catch(error => {
    console.log('Result:', error);
  });
