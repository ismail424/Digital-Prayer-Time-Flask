var all_inputs;
var translate_text = [];


function change_language( language ){

    all_inputs = document.getElementsByTagName("input")

    if(language == "usa"){
        translate_text = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Prayer","Begins","Iqamah","Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha","Next...","Please, turn off your phones!!!"];
    } 
    else if(language == "swe"){
        translate_text = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag", "Bön", "Börjar", "Iqamah", "Fajr", "Soluppgång","Dhuhr","Asr","Maghrib","Isha","Nästa ...","Snälla stäng av era telefoner!!!"];
    } 
    else if(language == "ba"){
        translate_text = ["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak", "Subota", "Nedjelja", "Namaz", "Počinje", "Ikamet", "Zora", "Izlazak sunca" , "Podne", "Ikindija", "Akšam", "Jacija", "Sljedeći...", "Isključite telefone!!!"];
    }else{return;}

    let x = 0;
    while (x < 18){
        all_inputs[x].value = translate_text[x];   
        x++;
    }
}