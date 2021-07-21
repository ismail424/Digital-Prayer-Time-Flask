//IP addres / QR code
var ip = "127.0.1.1";
var qrcode = new QRCode(document.getElementById("qrcode"), {text : "http://" + ip + "/", width: 128,height : 128});


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
var sec_all_day = 0;

//list with prayers (Secounds)
var prayer_list_sec = [];

//list with prayers (Names)
var prayer_list_name = [];

//list with prayers (Time)
var prayer_list_time = [];

//list with prayers (Time)
var prayer_id_list = ["fajr-time","sunrise-time","dhuhr-time","asr-time","maghrib-time","isha-time"];

//Check if iqamah is on
var iqamah_on = "false";



//Translation
var days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

var prayer = "Prayer";
var begins = "Begins";
var iqamah = "Iqamah";

var fajr_name = "Fajr";
var fajr_iqamah_name = fajr_name + iqamah;
var sunrise_name = "Sunrise";
var dhuhr_name = "Dhuhr";
var dhuhr_iqamah_name = dhuhr_name  + iqamah;
var asr_name  = "Asr";
var asr_iqamah_name = asr_name + iqamah;
var maghrib_name = "Maghrib";
var maghrib_iqamah_name = maghrib_name + iqamah;
var isha_name = "Isha";
var isha_iqamah_name = isha_name + iqamah;

var next_text = "Next...";
var footer_text = "Please, turn off your phones";


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
            iqamah_on = prayertime.iqamah_on;

            if (prayertime.iqamah_on == "true"){
                document.getElementById("sunrise-time").innerText = prayertime.sunrise
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
            }
            else{
                no_iqamah()
                document.getElementById("sunrise-time").innerText = prayertime.sunrise
                document.getElementById("fajr-time").innerText = prayertime.fajr
                document.getElementById("dhuhr-time").innerText = prayertime.dhuhr
                document.getElementById("asr-time").innerText = prayertime.asr
                document.getElementById("maghrib-time").innerText = prayertime.maghrib
                document.getElementById("isha-time").innerText = prayertime.isha
            }
            set_next_prayer_variable()
            setInterval(() => next_prayertime(),1000);
        }
        else {
            document.getElementById("error").style.display = "block";
        }
    } catch (error) {
        document.getElementById("error").style.display = "block";
        console.log(error);
    }


}


function no_iqamah(){
    
    document.getElementById("iqamah_text_section").classList.add("no_iqamah_text");
    document.getElementById("sunrise-time").style.flex = "50%";
    document.getElementById("sunrise_logo").style.margin = 0;
    document.getElementById("sunrise-h2").style.flex = "43%";
    document.getElementById("sunrise-h2").style.maxWidth = "43%";
    document.getElementById("sunrise-time").classList.add("background_color");

    document.getElementById("fajr-time-iqamah").style.display = "none";
    document.getElementById("dhuhr-time-iqamah").style.display = "none";
    document.getElementById("asr-time-iqamah").style.display = "none";
    document.getElementById("maghrib-time-iqamah").style.display = "none";
    document.getElementById("isha-time-iqamah").style.display = "none";

}

//init the variables that are going to be used
function set_next_prayer_variable(){
    if (iqamah_on == "true"){
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
        sec_all_day = new Date('1970-01-01T' + "24:00" + 'Z').getTime() / 1000;


        //Add to list (Sec)
        prayer_list_sec.push(sec_fajr);
        prayer_list_sec.push(sec_fajr_iqamah);
        prayer_list_sec.push(sec_sunrise);
        prayer_list_sec.push(sec_dhuhr);
        prayer_list_sec.push(sec_dhuhr_iqamah);
        prayer_list_sec.push(sec_asr);  
        prayer_list_sec.push(sec_asr_iqamah);  
        prayer_list_sec.push(sec_maghrib);  
        prayer_list_sec.push(sec_maghrib_iqamah);  
        prayer_list_sec.push(sec_isha);  
        prayer_list_sec.push(sec_isha_iqamah);

        //Add to list (Time)
        prayer_list_time.push(fajr);
        prayer_list_time.push(fajr_iqamah);
        prayer_list_time.push(sunrise);
        prayer_list_time.push(dhuhr);
        prayer_list_time.push(dhuhr_iqamah);
        prayer_list_time.push(asr);  
        prayer_list_time.push(asr_iqamah);  
        prayer_list_time.push(maghrib);  
        prayer_list_time.push(maghrib_iqamah);  
        prayer_list_time.push(isha);  
        prayer_list_time.push(isha_iqamah);

        //Add to list (name)
        prayer_list_name.push(fajr_name);
        prayer_list_name.push(fajr_iqamah_name);
        prayer_list_name.push(sunrise_name);
        prayer_list_name.push(dhuhr_name);
        prayer_list_name.push(dhuhr_iqamah_name);
        prayer_list_name.push(asr_name);  
        prayer_list_name.push(asr_iqamah_name);  
        prayer_list_name.push(maghrib_name);  
        prayer_list_name.push(maghrib_iqamah_name);  
        prayer_list_name.push(isha_name);  
        prayer_list_name.push(isha_iqamah_name);

    }
    else{
        sec_fajr = new Date('1970-01-01T' + fajr + 'Z').getTime() / 1000;
        sec_sunrise= new Date('1970-01-01T' + sunrise + 'Z').getTime() / 1000;
        sec_fajr_tomorrow = new Date('1970-01-01T' + fajr_tomorrow + 'Z').getTime() / 1000;
        sec_dhuhr = new Date('1970-01-01T' + dhuhr + 'Z').getTime() / 1000;
        sec_asr = new Date('1970-01-01T' + asr + 'Z').getTime() / 1000;
        sec_maghrib = new Date('1970-01-01T' + maghrib + 'Z').getTime() / 1000;
        sec_isha = new Date('1970-01-01T' + isha + 'Z').getTime() / 1000;

        //Add to list (Secounds)
        prayer_list_sec.push(sec_fajr);
        prayer_list_sec.push(sec_sunrise);
        prayer_list_sec.push(sec_dhuhr);
        prayer_list_sec.push(sec_asr);  
        prayer_list_sec.push(sec_maghrib);  
        prayer_list_sec.push(sec_isha);  

        //Add to list (Time)
        prayer_list_time.push(fajr);
        prayer_list_time.push(sunrise);
        prayer_list_time.push(dhuhr);
        prayer_list_time.push(asr);  
        prayer_list_time.push(maghrib);  
        prayer_list_time.push(isha);  

        //Add to list (Name)
        prayer_list_name.push(fajr_name);
        prayer_list_name.push(sunrise_name);
        prayer_list_name.push(dhuhr_name);
        prayer_list_name.push(asr_name);  
        prayer_list_name.push(maghrib_name);  
        prayer_list_name.push(isha_name);  
    }

}


//Next prayertime and countdown
async function next_prayertime(){

    var date = new Date()
    h = date.getHours();
    m = date.getMinutes();
    s = date.getSeconds();
    if(h<10){h = "0" + h;}
    if(m<10){ m = "0" + m;}
    if(s<10){s = "0" + s;}

    //Time now
    time_now = ''+h+':'+m+':'+s+'';

    //Convert time to secounds
    seconds_now = new Date('1970-01-01T' + time_now + 'Z').getTime() / 1000;

    let closest = prayer_list_sec.reduce((a, b) => {
        return Math.abs(b - seconds_now) < Math.abs(a - seconds_now) ? b : a;
    });
    let closest_index = prayer_list_sec.indexOf(closest);
    var closest_prayer_sec = prayer_list_sec[closest_index]
    let next_prayer_name = "";
    let next_prayer_time = "";
    let next_prayer_sec_left = 0;

    let list_length =  prayer_list_sec.length;
    if (closest_prayer_sec - seconds_now <= 0 ){
        
            if (closest_index == list_length - 1){
                next_prayer_name = prayer_list_name[0];
                next_prayer_time = fajr_tomorrow;
                let x =  86400 - seconds_now 
                next_prayer_sec_left = x + sec_fajr_tomorrow;
            }
            else{
                if (prayer_list_sec[closest_index + 1] == prayer_list_sec[closest_index] ){
                    if (closest_index + 2 != 11){

                    next_prayer_name = prayer_list_name[closest_index + 2];
                    next_prayer_time = prayer_list_time[closest_index + 2];
                    next_prayer_sec_left = prayer_list_sec[closest_index + 2] - seconds_now;
                    }
                    else{
                        next_prayer_name = prayer_list_name[0];
                        next_prayer_time = fajr_tomorrow;
                        let x =  86400 - seconds_now 
                        next_prayer_sec_left = x + sec_fajr_tomorrow;
                    }
                    
                }
                else{
                    
                    next_prayer_name = prayer_list_name[closest_index + 1];
                    next_prayer_time = prayer_list_time[closest_index + 1];
                    next_prayer_sec_left = prayer_list_sec[closest_index + 1] - seconds_now;
                } 
            }

    }
    else{
        next_prayer_name = prayer_list_name[closest_index];
        next_prayer_time = prayer_list_time[closest_index];
        next_prayer_sec_left = prayer_list_sec[closest_index] - seconds_now;
    }

    
    
    
    if (iqamah_on == "false"){
        for (temp_name in prayer_id_list) {
            try{ document.getElementById(prayer_id_list[temp_name]).style.backgroundColor = "";} catch(error) {console.log(error)}
        } 
        try {
            document.getElementById(prayer_id_list[closest_index]).style.backgroundColor = "transparent";} catch(error) {console.log(error)}

    }


    let min  = Math.floor(next_prayer_sec_left / 60),
    remSec  = next_prayer_sec_left % 60;
    let hour = Math.floor(min/ 60),
    remMin  = min % 60;
    if (remMin < 10) { remMin = '0' + remMin;}
    if (remSec < 10) { remSec = '0' + remSec;}
    if (hour < 10) {hour = '0' + hour;}
    timer = hour + ":" +remMin + ":" + remSec;
    
    // NEXT PRAYER DIV id
    var div_next_prayer = document.getElementById("next_prayer")
    var div_next_prayer_time = document.getElementById("next_prayer_time")
    var div_next_prayer_countdown = document.getElementById("next_prayer_countdown")

    div_next_prayer.innerText = next_prayer_name;
    div_next_prayer_time.innerText = next_prayer_time;
    div_next_prayer_countdown.innerText = timer;

    div_next_prayer_countdown.style.color = "#fff";

    if (next_prayer_sec_left < 900){div_next_prayer_countdown.style.color = "#e7b416";}
    if (next_prayer_sec_left < 600){div_next_prayer_countdown.style.color = "red";}
    if (next_prayer_sec_left <= 0) {div_next_prayer_countdown.innerHTML = '';}

}



async function get_translation(){
    try {
        const url = '/api/get_translation';
        let response = await fetch(url);
        var translate = await response.json();

        days = [ translate.sunday, translate.monday, translate.tuesday, translate.wednesday, translate.thursday, translate.friday, translate.saturday]

        prayer = translate.prayer;
        iqamah = translate.iqamah;
        begins = translate.begins;
        
        fajr_name = translate.fajr;
        fajr_iqamah_name = fajr_name  + " " + iqamah;
        sunrise_name = translate.sunrise;
        dhuhr_name = translate.dhuhr;
        dhuhr_iqamah_name = dhuhr_name  + " " +iqamah;
        asr_name  = translate.asr;
        asr_iqamah_name = asr_name + " " +iqamah;
    
        maghrib_name = translate.maghrib;
        maghrib_iqamah_name = maghrib_name + " " +iqamah;
        isha_name = translate.isha;
        isha_iqamah_name = isha_name + " " +iqamah;
        
        next_text = translate.next_text;
        footer_text = translate.footer_text;
        set_translation()
        current_day_name()
        fix_fontsize()


    } catch (error) {
        console.log(error);
    }



}
function set_translation(){
    document.getElementById("prayer").innerText =  prayer;
    document.getElementById("begins").innerText =  begins;
    document.getElementById("iqamah").innerText =  iqamah;

    document.getElementById("fajr").innerText = fajr_name;
    document.getElementById("sunrise-h2").innerText = sunrise_name;
    document.getElementById("dhuhr").innerText = dhuhr_name;
    document.getElementById("asr").innerText = asr_name;
    document.getElementById("mahgrib").innerText = maghrib_name;
    document.getElementById("isha").innerText = isha_name;

    document.getElementById("next_text").innerText = next_text;
    document.getElementById("footer_text").innerText = footer_text;


}

function current_day_name() {
    let a = new Date();
    let r = days[a.getDay()];
    document.getElementById("current_day_name").innerText = r;
}

async function create_qr_code(){
    const url = '/api/get_ip';
    let response = await fetch(url);
    var qr = await response.json();
    ip = qr.ip;
    if (qr.qrcode_on == "true"){
        qrcode.clear();
        qrcode.makeCode("http://" + ip + "/"); 
        document.getElementById("qrcode_ip").innerText = ip;
        document.getElementById("qrcode").style.display = "block";

    }
    else{
        document.getElementById("qrcode").style.display = "none";
        qrcode.clear();
        document.getElementById("qrcode_ip").innerText = ip;
    }

    if(ip == "127.0.1.1"){
        document.getElementById("qrcode").style.display = "none";
        document.getElementById("qrcode_ip").innerText = "";
    }

}


//--------------------SLIDE------------------------
var current_slideIndex = 0;
var slides = document.getElementsByClassName("slide-container");
var current_slide_height = 0;
var current_slide_delay = 30000;
var video_duration = 0;
var current_selected = "";

var url1 = ""
var url2 = ""
var video_url = ""
var google_slide_url = ""

function showSlides() {
  var i;
  if (slides.length == 1){
  	return;
  }
  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }

  if (current_slideIndex >= slides.length) {current_slideIndex = 0;}
  slides[current_slideIndex].style.display = "block";  

  if (current_slideIndex == 0){
    slides[0].style.height = null;
    slides[0].style.maxHeight = null;

    div_height = document.getElementById("slider-frame").offsetHeight;
    div_width = document.getElementsByClassName("slider-frame").offsetWidth;
    var y;
    for (y = 0; y < slides.length; y++) {
        slides[y].style.maxHeight = div_height + "px";
        slides[y].style.maxWidth = div_width + "px";
        slides[y].style.height = div_height + "px";
        slides[y].style.width = div_width + "px";

    }
  } 

  current_slideIndex++;
  
  if (current_selected == "video"){
    video_duration_now()
    setTimeout(showSlides, video_duration); 

  }
  else{
      setTimeout(showSlides, current_slide_delay); 
  }
}

async function init_slide(){ 

    const url = "/api/get_images"
    let response = await fetch(url);
    var images = await response.json(); 

    current_slide_delay = parseInt(images.slide_delay,10);
    current_slide_delay = current_slide_delay * 1000;
    current_selected = images.current_select;

    if (images.current_select == "none"){return;}
    else if (images.current_select == "images"){
        url1 = images.url_1;
        url2 = images.url_2;

        if (url1.length != 0){
            document.getElementById("slider-frame").innerHTML += '<div class="slide-container fade"><img src="./static/upload/'+url1+'" ></div> '
        }
        if (url2.length != 0){
            document.getElementById("slider-frame").innerHTML += '<div class="slide-container fade"><img src="./static/upload/'+url2+'" ></div> '
        }
    }
    else if (images.current_select == "video"){
        video_url = images.video_url;
        
        if (video_url.length != 0){
            document.getElementById("slider-frame").innerHTML += '<div class="slide-container fade"><video id="video" loop width="100%" height="100%" autoplay muted><source src="./static/upload/'+video_url+'" ></video></div> '
        }
    
    }
    else if (images.current_select == "google_slide"){
        google_slide_url = images.google_slide_url;
        
        if (google_slide_url.length != 0){
            document.getElementById("slider-frame").innerHTML += '<div class="slide-container fade">'+google_slide_url+'</div> ';
        }
    
    }
    else {return;}
    slides = document.getElementsByClassName("slide-container");
    showSlides();

}

function refreshAt(hours, minutes, seconds) {
    var now = new Date();
    var then = new Date();

    if(now.getHours() > hours ||
       (now.getHours() == hours && now.getMinutes() > minutes) ||
        now.getHours() == hours && now.getMinutes() == minutes && now.getSeconds() >= seconds) {
        then.setDate(now.getDate() + 1);
    }
    then.setHours(hours);
    then.setMinutes(minutes);
    then.setSeconds(seconds);

    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() { window.location.reload(true); }, timeout);
}

function video_duration_now(){var vid = document.getElementById("video");video_duration = vid.duration * 1000;}

create_qr_code()

//Run the functions
get_translation()
get_prayertimes()
fix_fontsize()
init_slide()
refreshAt(0,0,30); 

setInterval(() => current_time("current_time", ":"),1000);
setInterval(() => date_time("date_time", "-"),1000);
setInterval(() => create_qr_code(),5000);
setInterval(() => current_day_name(),5000);



