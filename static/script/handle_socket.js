var socket = io();

socket.on('refresh', () => {window.location.reload()});
socket.on('error_url', () => {alert("Error, The url is not working")});
socket.on('error_wifi', () => {alert("Error, You need wifi!")});
socket.on('success', () => {alert("New prayertimes set!")});



try {
    document.getElementById("save_prayertime").addEventListener("click", function() {
        var value = document.getElementById("city_islamiskaforbundet").value
        socket.emit('new-prayertime-salahtimes', {"data": value});
        alert("Saving prayertimes");
    })
} 
catch (error) {
    console.log(error)   
}

try {
    document.getElementById("save_prayertime2").addEventListener("click", function() {
        var value = document.getElementById("city").value
        socket.emit('new-prayertime-salahtimes2', {"data": value});
        alert("Saving...");
    })
} 
catch (error) {
    console.log(error)   
}

try {
    document.getElementById("save_prayertime3").addEventListener("click", function() {
        var value = document.getElementById("vaktija_eu_city").value;
        if (value != undefined || value != "") {
        socket.emit('new-prayertime-vaktijaeu', {"data": value});
        alert("Saving..." );
        }
        else {
            console.log(value);
            alert("Please enter a valid city name");
        }
    })
} 
catch (error) {
    alert("Try again!")
    console.log(error)   
}