const http = require("http")
const https = require("https")

const server = http.createServer((req, res) => {
   if (req.method === "GET") {
    if (req.url === "/ping") {
       // res.setHeader("Content-Type", "application/json")
       console.log(JSON.stringify({
        address: req.socket.remoteAddress,
        reqHeaders: req.headers
    }))
        res.write("pong")
        res.end()
    }
   }
})

server.listen(8080)