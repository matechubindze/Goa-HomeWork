let b=document.querySelectorAll("button")
b[0].onclick=()=>{let arr=[1,2];arr.unshift(0);alert(arr)}
b[1].onclick=()=>{let arr=[1,2,3];alert(arr.indexOf(2))}
b[2].onclick=()=>{let arr=[1,2,3];alert(arr.includes(2))}
b[3].onclick=()=>{let arr=[1,2,3];alert(arr.join("-"))}
b[4].onclick=()=>{let arr=[1,2,3];alert(arr.reverse())}
b[5].onclick=()=>{let arr=[1,2,3];alert(arr.sort())}
b[6].onclick=()=>{let arr=[1,2,3];alert(arr.slice(1))}
