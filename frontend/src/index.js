// Load or initialize visit counter
let visitCounter = parseInt(localStorage.getItem("visit_counter") || "0")

// Load or create a user ID 
let userId = localStorage.getItem("user_id")
console.log("Loaded user ID:", userId)
if (!userId) { // it does not exist then create
    userId = crypto.randomUUID()
    localStorage.setItem("user_id", userId)
    console.log("New user ID created:", userId)
}

// Increment visit counter and store it
visitCounter +=1
localStorage.setItem("visit_counter", visitCounter)

// Create the HTML content
let html = `
    It is your #${visitCounter} visit
`
// Display the content
document.getElementById('footer').innerHTML= html


fetch("http://127.0.0.1:8000/health")
.then(response => response.text())
.then(data=>console.log(data))

fetch("http://127.0.0.1:8000/echo",{method:"POST"})
.then(response => response.text())
.then(data => console.log(data))

fetch("http://127.0.0.1:8000/v1/visits",{
    method:"POST",
    body:JSON.stringify({userId:userId})
})
.then(response => response.json())
.then(data => console.log(data))


fetch("http://127.0.0.1:8000/v2/visits",{
    method:"POST",
    // send the userId in the body as JSON
    body:JSON.stringify({userId:userId})
})
.then(response => response.json())
.then(data => console.log(data))


fetch('http://127.0.0.1:8000/v2/visits?userId='+userId)
.then(response => response.json())
.then(data => console.log(data))

fetch('http://127.0.0.1:8000/v2/visits?dbID='+dbID)
.then(response => response.json())
.then(data => console.log(data))