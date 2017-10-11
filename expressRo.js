var express = require("express");
var bodyParser = require("body-parser");
var fs = require("fs");
var app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false });

fs.readFile("dataSet.txt", "utf8", function (err, data){
  if (err) throw err;
  else {
    weights = JSON.parse(data);
  }
  if (weights.status==="green") { status = "NO ACTIONS REQUIRED"}
  else {status = "IMMEDIATE ACTIONS REQUIRED"}
  app.get("/doctor", function (req, res) {
    res.render("disease", {weights1 : weights, status1:status});
  });
});

app.set("view engine", "ejs");

app.use(express.static("public"));

app.get("/health", function (req, res) {
  res.render("patient");
});

app.get("/qna", function (req, res) {
  res.render("qna");
});


app.post("/health",urlencodedParser, function (req, res) {
  console.log(req.body);
  var patient = req.body;
  res.render("patient");
  fs.appendFile("logged.txt", JSON.stringify(req.body.SYMPTOMS)+"\n\n", function(err){
    if(err) throw err;
    console.log('saved');
  });
});


app.listen(3000);
console.log("listening to port 3000");
