var appUrl = "http://127.0.0.1:5000/";

$(".submited").click(function(){
    console.log("clicked");

    var name = $("#name").val();
    var email = $("#email").val();
    var cont = $("#cont").val();
    var add = $("#add").val();
    var diag = $("#diag").val();
    var pass = $("#pass").val();

    var dataSend = {
        "async": true,
        "crossDomain": true,
        "url": appUrl + "register",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        },
        "processData": false,
        "data": "{\n\t\"name\": \"" + name + "\", \n\t\"email\": \"" + email + "\", \n\t\"cont\": \"" + cont + "\", \n\t\"add\": \"" + add + "\", \n\t\"diag\": \"" + diag + "\", \n\t\"pass\": \"" + pass + "\"}"
    }
    $.ajax(dataSend).done(function (response) {
        console.log("done")
        alert("You have been registered!!!");
        window.location.replace("./index.html");
    });
});