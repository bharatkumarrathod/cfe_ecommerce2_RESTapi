$(document).ready(function(){

    function setPrice(){

        var price = $('.variation_select option:selected').attr('data-price');
        var sale_price = $('.variation_select option:selected').attr('data-sale-price');

        if (sale_price != "" && sale_price != "None" && sale_price != null){
            $('#price').html("<h3>" + sale_price + " <small class='original-price'>" + price + "</small></h3>");
        } else {
            $('#price').html(price);
        }
    }

    setPrice();

    $('.variation_select').change(function(){
        setPrice();
    });

});