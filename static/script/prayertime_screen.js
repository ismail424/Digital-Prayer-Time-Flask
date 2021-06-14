//Set variable
var fajr = "";
var fajr_iqamah = "";
var sunrise = "";
var dhuhr = "";
var dhuhr_iqamah = "";
var asr = "";
var asr_iqamah = "";
var maghrib = "";
var maghrib_iqamah = "";
var isha = "";
var isha_iqamah = "";
var fajr_tomorrow = "";


var seconds_now = 0;
var sec_fajr = 0;
var sec_fajr_iqamah = 0;
var sec_sunrise= 0;
var sec_fajr_tomorrow = 0;
var sec_dhuhr = 0;
var sec_dhuhr_iqamah = 0;
var sec_asr = 0;
var sec_asr_iqamah = 0;
var sec_maghrib = 0;
var sec_maghrib_iqamah = 0;
var sec_isha = 0;
var sec_isha_iqamah = 0;

// NEXT PRAYER DIV id
var next_prayer = document.getElementById("next_prayer")
var next_prayer_time = document.getElementById("next_prayer_time")
var next_prayer_countdown = document.getElementById("next_prayer_countdown")




//Current time (LIVE CLOCK)
async function current_time( id , tecken ){
    var today = new Date();
    let hours = today.getHours()
    let minutes = today.getMinutes()
    let sekunder = today.getSeconds()
    var time  = ("0" + hours).substr(-2) + tecken + ("0" + minutes).substr(-2) + tecken + ("0" + sekunder).substr(-2);
    document.getElementById(id).innerHTML = time;    
}

//Current date (GET CURRENT DATE)
async function date_time( id , tecken ){
    var today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    
    date =  yyyy + tecken + mm + tecken + dd ;
    document.getElementById(id).innerHTML = date;
}

//Fix font-size
async function fix_fontsize(){
    try{
        var sunrise_text = document.getElementById("sunrise-h2").innerHTML
        if(( sunrise_text.length > 8 ) &&( sunrise_text.length <= 11 )){
            document.getElementById("sunrise-h2").style.fontSize = "5vw";
        }
        else if (( sunrise_text.length > 11) && ( sunrise_text.length <= 13)){
            document.getElementById("sunrise-h2").style.fontSize = "4vw";
        }
        else if (( sunrise_text.length > 13)){
            document.getElementById("sunrise-h2").style.fontSize = "3vw";
        }
        return null;

    }
    catch{
        return null;
    }

}


//Fetch API 
async function  get_prayertimes(){
    try {
        const url = '/api/get_prayertimes';
        let response = await fetch(url);
        var prayertime = await response.json(); 

        //Check for error's
        if (prayertime.error == "false"){

            fajr = prayertime.fajr;
            fajr_iqamah = prayertime.fajr_iqamah;
            sunrise = prayertime.sunrise;
            dhuhr = prayertime.dhuhr;
            dhuhr_iqamah = prayertime.dhuhr_iqamah;
            asr = prayertime.asr;
            asr_iqamah = prayertime.asr_iqamah;
            maghrib = prayertime.maghrib;
            maghrib_iqamah = prayertime.maghrib_iqamah;
            isha = prayertime.isha;
            isha_iqamah = prayertime.isha_iqamah;
            fajr_tomorrow = prayertime.fajr_tomorrow;

            document.getElementById("sunrise").innerText = prayertime.sunrise
            document.getElementById("fajr-time").innerText = prayertime.fajr
            document.getElementById("dhuhr-time").innerText = prayertime.dhuhr
            document.getElementById("asr-time").innerText = prayertime.asr
            document.getElementById("maghrib-time").innerText = prayertime.maghrib
            document.getElementById("isha-time").innerText = prayertime.isha
            document.getElementById("fajr-time-iqamah").innerText = prayertime.fajr_iqamah
            document.getElementById("dhuhr-time-iqamah").innerText = prayertime.dhuhr_iqamah
            document.getElementById("asr-time-iqamah").innerText = prayertime.asr_iqamah
            document.getElementById("maghrib-time-iqamah").innerText = prayertime.maghrib_iqamah
            document.getElementById("isha-time-iqamah").innerText = prayertime.isha_iqamah
            next_prayertime()
        }
        else {
            document.getElementById("error").style.display = "block";
        }
        console.log(prayertime);
    } catch (error) {
        document.getElementById("error").style.display = "block";
        console.log(error)
    }


}


//Next prayertime and countdown
function next_prayertime(){
    var date = new Date()
    h = date.getHours();
    m = date.getMinutes();
    s = date.getSeconds();
    if(h<10){h = "0" + h;}
    if(m<10){ m = "0" + m;}
    if(s<10){s = "0" + s;}

    //Time now
    time_now = ''+h+':'+m+':'+s+'';

    //Convert time to sekounds
    seconds_now = new Date('1970-01-01T' + time_now + 'Z').getTime() / 1000;
    sec_fajr = new Date('1970-01-01T' + fajr + 'Z').getTime() / 1000;
    sec_fajr_iqamah = new Date('1970-01-01T' + fajr_iqamah + 'Z').getTime() / 1000;
    sec_sunrise= new Date('1970-01-01T' + sunrise + 'Z').getTime() / 1000;
    sec_fajr_tomorrow = new Date('1970-01-01T' + fajr_tomorrow + 'Z').getTime() / 1000;
    sec_dhuhr = new Date('1970-01-01T' + dhuhr + 'Z').getTime() / 1000;
    sec_dhuhr_iqamah = new Date('1970-01-01T' + dhuhr_iqamah + 'Z').getTime() / 1000;
    sec_asr = new Date('1970-01-01T' + asr + 'Z').getTime() / 1000;
    sec_asr_iqamah = new Date('1970-01-01T' + asr_iqamah + 'Z').getTime() / 1000;
    sec_maghrib = new Date('1970-01-01T' + maghrib + 'Z').getTime() / 1000;
    sec_maghrib_iqamah = new Date('1970-01-01T' + maghrib_iqamah + 'Z').getTime() / 1000;
    sec_isha = new Date('1970-01-01T' + isha + 'Z').getTime() / 1000;
    sec_isha_iqamah = new Date('1970-01-01T' + isha_iqamah + 'Z').getTime() / 1000;



    // var vilken = "";
    // var bönbön = "";
    // const needle = seknu;
    // var closest2 = [sekfajr, sekzuhr, sekasr,  sekmagrib, sekisha];
    // const closest = [sekfajr, sekzuhr, sekasr,  sekmagrib, sekisha].reduce((a, b) => {
    //     return Math.abs(b - needle) < Math.abs(a - needle) ? b : a;
    // });
    // closest2 = closest;
    // function myFunction(hittanum) {
    // var a_a = [sekfajr, sekzuhr, sekasr,  sekmagrib, sekisha];
    // var a = a_a.indexOf(hittanum);
    // return a;
    // }
    // if ((closest - needle)<0){
    // var resulatindex = myFunction(closest);
    // var vilken_index = resulatindex;
    // var sistabön = resulatindex;
    // resulatindex = resulatindex + 1;
    // if (sistabön == 9){
    //     resulatindex = 0
    // }
    // closest2 = [sekfajr, sekzuhr, sekasr,  sekmagrib, sekisha];
    // closest2 = closest2[resulatindex];
    // }
    // sec = closest2 - seknu
    // if (closest2 == sekfajr){vilken = "{{post.fajrname}}"; document.getElementById("fajrcolor").style.backgroundColor = "#3d3d3d"; bönbön = fajr;}
    // if (closest2 == sekzuhr){vilken = "{{post.dhuhrname}}";document.getElementById("zuhrcolor").style.backgroundColor = "#3d3d3d";bönbön = zuhr;}
    // if (closest2 == sekasr){vilken = "{{post.asrname}}";bönbön = asr;document.getElementById("asrcolor").style.backgroundColor = "#383838";}
    // if (closest2 == sekmagrib){vilken = "{{post.magribname}}";document.getElementById("magribcolor").style.backgroundColor = "#3d3d3d";bönbön = magrib;}
    // if (closest2 == sekisha){vilken = "{{post.ishaname}}";bönbön = isha;document.getElementById("ishacolor").style.backgroundColor = "#383838";}
    // if (sistabön == 4){vilken = "{{post.fajrname}}"; document.getElementById("fajrcolor").style.backgroundColor = "#3d3d3d";bönbön = fajrimon;}
    // DIV2.innerHTML = vilken;
    // DIV3.innerHTML = bönbön;
    // var min  = Math.floor(sec / 60),
    // remSec  = sec % 60;
    // var hour = Math.floor(min/ 60),
    // remMin  = min % 60;
    // if (remMin < 10) {
        
    //     remMin = '0' + remMin;
    // }
    // if (remSec < 10) {
        
    //     remSec = '0' + remSec;
    // }
    // if (hour < 10) {
        
    //     hour = '0' + hour;
    // }
    // document.getElementById("bönklocka").style.color = "#fff";
    // DIV.innerHTML = hour + ":" +remMin + ":" + remSec;
    
    
    // if (sec < 900){
    // document.getElementById("bönklocka").style.color = "#e7b416";
    // }
    // if (sec < 600){
    // document.getElementById("bönklocka").style.color = "red";
    // }
    // if (sec > 0) {
        
    //     sec = sec - 1;
        
    // } else {
        
    //     DIV.innerHTML = '';
    
        
    // }

    // //set timeout
    // setTimeout('bönklocka();','1000');
    // }


}

//Run the functions
get_prayertimes()
fix_fontsize()
setInterval(() => current_time("current_time", ":"),1000);
setInterval(() => date_time("date_time", "-"),1000);