console.log("connected");

var appUrl = "http://127.0.0.1:5000/";



var selectedNames = {
    "async": true,
    "crossDomain": true,
    "url": appUrl + "getData",
    "method": "GET",
    "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
    },
    "processData": false,
    "data": "{}"
}

$.ajax(selectedNames).done(function (response) {
    console.log(response);
});