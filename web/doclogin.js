var appUrl = "http://127.0.0.1:5000/";

$("#submit").click(function(){
    console.log("clicked");

    var email = $("#email").val();
    var pass = $("#pass").val();
    console.log(email, pass);

    var dataSend = {
        "async": true,
        "crossDomain": true,
        "url": appUrl + "DocLogin",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        },
        "processData": false,
        "data": "{\n\t\"email\": \"" + email + "\", \n\t\"pass\": \"" + pass + "\"}"
    }
    $.ajax(dataSend).done(function (response) {
        console.log(response);

        if(response["valid"] == "true")
            window.location.replace("./Doctorrec.html");
        else
            alert("Incorect Eamil or Password!!!")
    });
});