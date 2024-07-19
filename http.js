const http = require('http');
const fs = require('fs');
const path = require('path');
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    console.log('request received');
    console.log(req.headers.referer);

    let filePath = 'templates' + (req.url === '/' ? '/index.html' : req.url);
    filePath = path.join(__dirname, filePath);

    fs.readFile(filePath, (error, data) => {
        if (error) {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('404 Not Found');
        } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(data);
        }
    });
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
});
