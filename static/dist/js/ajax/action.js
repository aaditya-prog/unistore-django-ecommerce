$(document).ready(function () {
    $('.item-qty').change(function () {
        var cartRows = document.getElementsByClassName("cart-border");
        total_price = 0;
        for (var i = 0; i < cartRows.length; i++) {
            total = 0
            total_quantity = 0
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName('cart-price')[0]
            var quantityElement = cartRow.getElementsByClassName('item-qty')[0]
            var price = parseFloat(priceElement.innerText.replace('$', ''))
            var quantity = quantityElement.value
            total_price += (price * quantity)
        }
        document.getElementById("total_price").innerHTML = "&nbsp;" + total_price;
    });
});
