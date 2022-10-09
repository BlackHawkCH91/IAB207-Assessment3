function updatePrice() {
    //Get input value and output text
    var input = document.getElementById("ticketNumber");
    var output = document.getElementById("ticketPrice");

    //Set price
    output.innerHTML = "Total price: $" + input.value * 30;
}