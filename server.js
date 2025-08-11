// server.js
const http = require('http');
const hostname = '0.0.0.0';
const port = process.env.PORT || 8080;

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify({ status: 'OK', time: new Date().toISOString() }));
  } else {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello from Student CI/CD Pipeline Demo!');
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
