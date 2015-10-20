function addProductNameToMessage(message) {

    var productTitle = $("#product-title").text();
    var variationTitle = $(".variation-title").text();

    if (productTitle != null && variationTitle != null && productTitle != "" && variationTitle != "") {
        message = "<strong>" + productTitle + "</strong>" + " - " + "<strong>" + variationTitle + "</strong>" + " " + message;
    } else if (productTitle != null && variationTitle == null && productTitle != "") {
        message = "<strong>" + productTitle + "</strong>" + " " + message;
    } else {
        message = message;
    }
//console.log(message);
    return message;
}