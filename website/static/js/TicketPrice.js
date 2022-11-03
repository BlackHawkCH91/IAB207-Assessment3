function updatePrice(ticketPrice) {
    //Get input value and output text
    var input = document.getElementById("ticketNumber");
    var output = document.getElementById("ticketPrice");

    console.log(input.value);
    console.log(ticketPrice);
    //Set price
    output.innerHTML = "Total price: $" + input.value * ticketPrice;
}