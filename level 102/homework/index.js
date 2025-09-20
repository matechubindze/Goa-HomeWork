let b=document.querySelectorAll("button")
b[0].onclick=()=>{let arr=[1,2,3,4,5];alert(arr.filter(x=>x%2==0))}
b[1].onclick=()=>{let arr=[1,2,3,4];alert(arr.reduce((a,c)=>a+c,0))}
b[2].onclick=()=>{let arr=[1,2,3,4];alert(arr.every(x=>x>0))}
b[3].onclick=()=>{let arr=[1,2,3,4];alert(arr.some(x=>x>3))}
b[4].onclick=()=>{let arr=["a","b","c"];for(let [i,v] of arr.entries())console.log(i,v)}
b[5].onclick=()=>{let arr=[1,2,3];alert(Array.isArray(arr))}
b[6].onclick=()=>{let arr=[1,2,3];alert(arr.find(x=>x>2))}
b[7].onclick=()=>{let arr=[1,2,3];alert(arr.findIndex(x=>x>2))}
