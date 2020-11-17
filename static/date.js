function date_time2(id)
{
        date = new Date;
        year = date.getFullYear();
        month = date.getMonth();
        months = new Array('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12');
        d = date.getDate();
        day = date.getDay();
        tecken = ("-");
        days = new Array('Söndag', 'Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag');
        h = date.getHours();
        if(h<10)
        {
                h = "0"+h;
        }
        m = date.getMinutes();
        if(m<10)
        {
                m = "0"+m;
        }
        s = date.getSeconds();
        if(s<10)
        {
                s = "0"+s;
        }
        result = ''+days[day]+' '+year+''+tecken+'' +months[month]+''+tecken+''+d+'';
        document.getElementById(id).innerHTML = result;
        setTimeout('date_time2("'+id+'");','1000');
        return true;
}