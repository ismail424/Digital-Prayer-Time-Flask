console.log("Fetching all the API data");

var countries = [

];
const check_if_contains = (array, value) => {
    for(let x = 0; x < array.length; x++) {
        if(array[x].name === value) {
            return true;
        }
    }
    return false;
}

const vaktija_eu = async () =>    {
    let regionNames = new Intl.DisplayNames(['en'], {type: 'region'});
    console.log("Fetching vaktija.eu");
    response = await fetch("/get_vaktija_eu");
    data = await response.json();
    if (data.error) {
        alert("Error fetching vaktija.eu\nPlease try again later.\nIf the problem still exists, contact me cicas03@hotmail.com");
    }
    else {
        for(let i = 0; i < data.data.length; i++) {
            let vaktija = data.data[i];
            let vaktija_slug = vaktija.slug;
            let vaktija_name = vaktija.name;
            let vaktija_country_code = vaktija.country.short_code;
            let full_country_name = regionNames.of(vaktija_country_code);
            if (check_if_contains(countries, full_country_name) != true) {
                countries.push({
                    "name": full_country_name,
                    "cities": [
                        {"name": vaktija_name, "slug": vaktija_slug}
                    ]
                });
            }
            else {
                countries.find(x => x.name == full_country_name).cities.push({"name": vaktija_name, "slug": vaktija_slug});
            }
        }
        console.log("Successfully fetched vaktija.eu");

        let select = document.getElementById("vaktija_eu_country");
        countries = countries.sort((a, b) => (a.name > b.name) ? 1 : -1);
        for (let i = 0; i < countries.length; i++) {
            let option = document.createElement("option");
            option.text = countries[i].name;
            option.value = countries[i].name;
            select.appendChild(option);
            select.add(option);
        }
        select.addEventListener("change", function() {
                let cities = countries.find(x => x.name == this.value).cities;
                let select_city = document.getElementById("vaktija_eu_city");
                let vaktija_name = document.getElementById("vaktija_eu_name");
                vaktija_name.style.display = "block";
                select_city.style.display = "block";
                select_city.innerHTML = "";

                for(let i = 0; i < cities.length; i++) {
                    let option = document.createElement("option");
                    option.text = cities[i].name;
                    option.value = cities[i].slug;
                    select_city.appendChild(option);
                    select_city.add(option);
                }


        });
    }

}
vaktija_eu();

// fetch("/get_vaktija_eu")
//     .then(response => response.json())
    
// .then(data => {
//     console.log(data);
//     let select = document.getElementById("vaktija_eu_country");
//     for (let i = 0; i < data.length; i++) {
//         console.log(data[i]);
//         // let option = document.createElement("option");
//         // option.text = data[i].name;
//         // option.value = data[i].id;
//         // select.add(option);
//     }
// })
// .catch(error => alert("Error: " + error + "\nPlease try again later.\nIf the problem still exists, contact me cicas03@hotmail.com"));

