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
