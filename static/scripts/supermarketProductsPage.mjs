async function init_buttons () {
    let quantities = document.getElementsByClassName("quantity_fields");
    let buttons = document.getElementsByClassName("submit_buttons");
    console.log(quantities)
    console.log(buttons)
    for (let index = 0; index < buttons.length; index++) {
        buttons[index].addEventListener("click", (evt => add_product_to_cart(quantities[index].id, quantities[index].value) ))
    }
}


async function add_product_to_cart(product_id,quantity) {
    await apiGet(`/add_products/${product_id}/${quantity}`);
}

await init_buttons();