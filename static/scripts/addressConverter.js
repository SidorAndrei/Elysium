

function showAddress() {
    let results = document.querySelector("#results")

    if (addressArr.length > 0) {
        addressArr.forEach(element => {
            results.innerHTML +=  "<div class='results'>"
                                            + element.display_name
                                            + "<br> Lat: " + element.lat
                                            + " Lng: " + element.lon
                                            + "</div>"
        })
    }
    else {
        results.innerHTML  = "<p style='color: red;'>Not found</p>"
    }
}

async function findAddress() {
    apiGet(`/api/address`).then(result => result.address.forEach(a => {
        let url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + a.address
        console.log(url)
        console.log(a)
        fetch(url)
            .then(response => response.json())
            .then(data => addressArr = data)
            .then(show => {console.log(show[0].lat); console.log(show[0].lon);

            })
            .catch(err => console.log(err))
    } ))

}

