let count = 0;
let interval = setInterval(function () {
  let now = new Date();
  let formatted = now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate() +
     ", " + now.getHours() + "-" + now.getMinutes() + "-" + now.getSeconds();
  console.log(formatted);

  count++;
  if (count === 60) clearInterval(interval);
}, 1000);
