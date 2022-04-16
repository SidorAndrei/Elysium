function initMap() {
  let options = {
      center: {lat:44.4268, lng:26.1025},
      zoom:12
  }
  let map = new google.maps.Map(document. getElementById("map"), options)
    function addMarker(property){
    const marker = new google.maps.Marker(
      {position:property.location,
          map:map})

        const detailWindow = new google.maps.InfoWindow({
            content: `<h1>${property.name}</h1>
                        <h3>${property.address}</h3>`
        })
        marker.addListener("mouseover", () => {
            detailWindow.open(map, marker);
        })
        marker.addListener("mouseout", () => {
            detailWindow.close(map, marker);
        })
        marker.addListener("click", () => {
            go_to_supermarket_page(property.id).then(r =>
            {});
        })
    }

    async function findAddress() {
        apiGet(`/api/address`).then(result => result.address.forEach(a => {
            let url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + a.address
            console.log(url)
            console.log(a);
            let property = {address: a.address, id: a.supermarket_id, name: a.name}
            fetch(url)
                .then(response => response.json())
                .then(data => addressArr = data)
                .then(show => {
                    console.log(show[0].lat); console.log(show[0].lon);
                    property.location= {lat:parseFloat(show[0].lat), lng: parseFloat(show[0].lon)};
                    addMarker(property);
                })

        } ))

}

    findAddress().then();

}

async function go_to_supermarket_page(supermarket_id){
    document.querySelector('body').innerHTML += `<form id="form_red" method=post action='/supermarket/${supermarket_id}'></form>`;
    document.querySelector('#form_red').submit();
}
