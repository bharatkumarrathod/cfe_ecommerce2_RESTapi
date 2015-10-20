$(document).ready(function(){

    $("#submit-btn").click(function(event){
        event.preventDefault();
        var formData = $("#add-form").serialize();
        var cartUrl = $("#add-form").attr('action');
            while(cartUrl == null){
                cartUrl = $("#add-form").attr('action');
            }
        console.log(formData);

        $.ajax({
            type: "GET", // "POST"
            url: cartUrl,
            data: formData,
            success: function(data) {
                //showFlashMessage(data.flash_message);
                //updateCartItemCount();
                showFlashMessage("<strong>" + data.item_title + "</strong>" + " added to cart");
                updateCartItemCount();
            },
            error: function(response, error) {
                // console.log(response)
                // console.log(error)
                $("#add-form").submit()
            }
        })
    });

});