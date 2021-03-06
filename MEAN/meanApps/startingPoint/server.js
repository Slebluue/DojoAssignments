var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var app = express();
app.use(bodyParser.json());
app.use(express.static(__dirname+'/notes/dist'));

require('./server/config/mongoose.js');

var routes = require('./server/config/routes')
routes(app);

app.listen(8000, function(){
    console.log('====LISTENING ON PORT 8000====')
})