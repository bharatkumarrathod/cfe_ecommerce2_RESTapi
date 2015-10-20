function updateCartItemCount(){
    var badge = $("#cart-count-badge");

    $.ajax({
        type: "GET",
        url: "{% url 'item_count' %}",
        success: function(data){
            badge.text(data.count);
        },
        error: function(response, error){
            console.log(response);
            console.log(error);
        }
    })
}


$(document).ready(function(){

    updateCartItemCount();

});