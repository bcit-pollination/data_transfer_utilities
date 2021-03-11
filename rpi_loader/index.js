const controller = require('./export_controller');
const express = require('express');
const app = express();
const path = require('path');


// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/dataImport', function(req, res) {
  
    const pathname = req.query.pathName + "/";
    console.log(pathname );
    controller.runImport("./testing.key", pathname).then((data) => {
        console.log(data);
        res.json(data);
    }).catch((e) => console.log(e));

});

app.get('/dataExport', function(req, res) {
  
    const pathname = req.query.pathName + "/";
    console.log(pathname );
    controller.runExport("./test.json", "./testing.key", pathname).then((data) => {
        console.log(data);
        res.json(data);
    }).catch((e) => console.log(e));

});

app.get('/usbs', function(req, res) {
    controller.runUsbFetcher().then((data) => {
        console.log(data);
        res.json(data);
    }).catch((e) => console.log(e));
});

app.get('/import', function(req, res) {
    res.sendFile(path.join(__dirname + '/pages/import.html'));
});

app.get('/export', function(req, res) {
    res.sendFile(path.join(__dirname + '/pages/export.html'));
});

app.listen(8080);