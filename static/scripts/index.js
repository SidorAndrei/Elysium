console.log("aaaaaaaaa")

function initMap() {
  let options = {
      center: {lat:44.4268, lng:26.1025},
      zoom:12
  }
  let map = new google.maps.Map(document. getElementById("map"), options)

  const marker = new google.maps.Marker(
  {position:{lat:44.4082383, lng:26.178878211280374},
      map:map})

    const detailWindow = new google.maps.InfoWindow({
        content: `<div class="supermarkets" id="1">noi castigam</div>`
    })
    marker.addListener("mouseover", () => {
        detailWindow.open(map, marker);
    })
    marker.addListener("mouseout", () => {
        detailWindow.close(map, marker);
    })
    // marker.addListener("mouseout", () => {
    //     detailWindow.close(map, marker);
    // })
}

function go_to_supermarket_page(supermarket_id){

}