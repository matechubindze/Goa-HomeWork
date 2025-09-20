let b=document.querySelectorAll("button")
b[0].onclick=()=>{let arr=[1,2,3];arr.splice(1,1);alert(arr)}
b[1].onclick=()=>{let arr=[1,2,3];arr.splice(1,0,5);alert(arr)}
b[2].onclick=()=>{let arr=[1,2,3];alert(arr.toString())}
b[3].onclick=()=>{let arr1=[1,2],arr2=[3,4];alert(arr1.concat(arr2))}
b[4].onclick=()=>{let arr=[1,2,3];for(let x of arr)console.log(x)}
b[5].onclick=()=>{let arr=[1,2,3];for(let i in arr)console.log(i)}
b[6].onclick=()=>{let arr=[1,2,3];alert(arr.map(x=>x*2))}
