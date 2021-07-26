var socket = io();

socket.on('refresh', () => {window.location.reload()});
socket.on('error_url', () => {alert("Error, The url is not working")});
socket.on('error_wifi', () => {alert("Error, You need wifi!")});
socket.on('success', () => {alert("New prayertimes set!")});



try {
    document.getElementById("save_prayertime").addEventListener("click", function() {
        var value = document.getElementById("salahtimes_url").value
        socket.emit('new-prayertime-salahtimes', {"data": value});
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