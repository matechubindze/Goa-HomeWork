const executorFunction(resolve, reject) => {
    num = Math.random
    if (num >= 0.5){
        resolve("Heads!")
    }else{
        reject("Tails!")
    }

}
console.log(executorFunction)