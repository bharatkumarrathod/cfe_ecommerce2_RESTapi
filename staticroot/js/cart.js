$(document).ready(function(){

    $(".item-qty").change(function(){
        //vent.preventDefault();
        var item = $(this).prev("input[type='hidden']").val();
        var qty =  $(this).val();
        var data = {
            item: item,
            qty: qty
        };
        console.log(data);

        //var cartUrl = "http://127.0.0.1:8000/cart/"
        var cartUrl = $("#cart-form").attr('url');
        while( cartUrl == null){
            cartUrl = $("#cart-form").attr('url');
        }

        $.ajax({
           type: "GET",
            url: cartUrl,
            data: data,
            success: function(data){
                //$("#jquery-message").text("Added " + data.item_added + " Delete " + data.deleted);
                if(data.deleted){
                    $("#item-"+item).fadeOut();
                    showFlashMessage("Item removed from cart");
                } else {
                    $("#item-line-total-"+item).text(data.line_total);
                    $("#subtotal").text(data.subtotal);
                    showFlashMessage("Your cart has been updated");
                }

                if(data.total_items == 0){
                    $(".table").fadeOut()
                    $("#cart-container").load("carts/empty_cart.html")
                }
            },
            error: function(response, error) {
                console.log(response);
                console.log(error);
            }
        });

        // /$("#add-form").submit();
    })


});