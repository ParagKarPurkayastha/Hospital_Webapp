console.log("connected");

var appUrl = "http://127.0.0.1:5000/";

var dataGet = {
    "async": true,
    "crossDomain": true,
    "url": appUrl + "loginData",
    "method": "POST",
    "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
    },
    "processData": false,
    "data": "{}"
}
$.ajax(dataGet).done(function (response) {
    console.log("done : ", response["loginData"])
    document.getElementById("name").innerHTML = response["loginData"]["name"];
    document.getElementById("diag").innerHTML = response["loginData"]["diag"];
});