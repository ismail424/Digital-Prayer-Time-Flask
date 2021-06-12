//Current time (LIVE CLOCK)
function current_time( id , tecken ){
    var today = new Date();
    let hours = today.getHours()
    let minutes = today.getMinutes()
    let sekunder = today.getSeconds()
    var time  = ("0" + hours).substr(-2) + tecken + ("0" + minutes).substr(-2) + tecken + ("0" + sekunder).substr(-2);
    document.getElementById(id).innerHTML = time;    
}

//Current date (GET CURRENT DATE)
function date_time( id , tecken ){
    var today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    
    date =  yyyy + tecken + mm + tecken + dd ;
    document.getElementById(id).innerHTML = date;
}

function fix_fontsize(){
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

fix_fontsize()
setInterval(() => current_time("current_time", ":"),1000);
setInterval(() => date_time("date_time", "-"),1000);