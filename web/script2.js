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
    console.log(response["doctorData"]);
    $('.data').html(`
    <h1>`+ response["doctorData"]["name"] +`</h1>
    <hr>
    <h2>Specialization: <span class="Color">`+ response["doctorData"]["specialization"] +`</span></h2>
    <h2>Designation: <span class="Color">`+ response["doctorData"]["designation"] +`</span></h2>
    
    <h2>Qualifications:</h2>
    <ul class="Alum">
        <li>`+ response["doctorData"]["qualifications1"] +`</li>
        <li>`+ response["doctorData"]["qualifications2"] +`</li>
    </ul>

    <h2>Medical Experience:</h2>
    <ol class="Bio">
        <li>`+ response["doctorData"]["medical_experience1"] +`</li>
        <li>`+ response["doctorData"]["medical_experience2"] +`</li>
    </ol>

    <h2>Administrative Experience:</h2>
    <ol class="Exp">
        <li>`+ response["doctorData"]["administrative_experience1"] +`</li>
        <li>`+ response["doctorData"]["administrative_experience2"] +`</li>
    </ol>
    `);
});