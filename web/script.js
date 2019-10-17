console.log("connected");

var appUrl = "http://127.0.0.1:5000/";

var doctorsNames = {
    "async": true,
    "crossDomain": true,
    "url": appUrl + "doctorNames",
    "method": "GET",
    "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache"
    },
    "processData": false,
    "data": "{}"
}

$.ajax(doctorsNames).done(function (response) {
    // console.log(response);
    $('.doctorNames').html("");

    for (i = 0; i < response["doctor_names"].length; i++) {
        var name = response["doctor_names"][i]["name"];
        $('.doctorNames').append(`<a class="dropdown-item" href="./webpage.html" value="` + name + `"> ` + name + `</a>`);
        // <a class="dropdown-item" href="#">Dr. S. Srinavsan</a>
    }

});


$(".doctorNames").click(function (e){
    var txt = $(e.target).text();
    // console.log(txt);

    var setName = {
        "async": true,
        "crossDomain": true,
        "url": appUrl + "selectDoctor",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        },
        "processData": false,
        "data": "{\n\t\"name\": \"" + txt + "\"}"
    }
    $.ajax(setName).done(function (response) {
        console.log("done")
    });

});