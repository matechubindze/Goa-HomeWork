// საკლასო დავალება:

// Create a Promise that resolves after 
// 3 seconds with the message
//  "Task complete" using setTimeout.
const task = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Task Completed")
    } , 3000)
})