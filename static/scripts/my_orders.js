async function add_order() {
    let orders = await apiGet('/api/orders');
    for(let order of orders.orders){
        let products = await apiGet(`/api/get-cart-products/${order.cart_id}`);
        let div = `<div class="card">`
        for(let product of products.products){
            div += `<div class="card-row">
                <div class="product">
                    ${product.name}
                <span>${product.quantity} bucati</span>
            </div>
            </div>`
        }
        div += `</div>`;
        if(div !== `<div class="card"></div>`)
            document.querySelector('#main_cards_div').innerHTML += div;
    }
}

add_order().then(r => {});