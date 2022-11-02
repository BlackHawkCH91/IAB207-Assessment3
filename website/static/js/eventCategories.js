function SportCategories() {
    var enabled = [];
    var select = document.getElementById("citySelect");
    var city = select.options[select.selectedIndex].text;
    console.log(city);

    //Get checkboxes
    for (var i = 0; i < 8; i++) {
        if (document.getElementsByClassName("catCheckbox")[i].checked) {
            enabled.push(i + 1);
        }
    }

    var allItems = document.getElementsByClassName("eventItems");

    //If selected
    if (enabled.length > 0) {
        //Hide everything first
        for (var i = 0; i < allItems.length; i++) {
            allItems[i].style.display = "none";
        }

        //Enable categories
        for (var i = 0; i < enabled.length; i++) {
            var enabledItems = document.getElementsByClassName("category" + enabled[i]);
            

            for (var i2 = 0; i2 < enabledItems.length; i2++) {
                if (enabledItems[i2].getAttribute("data-city") == city || city == "All") {
                    enabledItems[i2].style.display = "block";
                    continue;
                }
                enabledItems[i2].style.display = "none";
            }
        }

        return;
    }

    //Show everything if nothing is selected
    for (var i = 0; i < allItems.length; i++) {
        if (allItems[i].getAttribute("data-city") == city || city == "All") {
            allItems[i].style.display = "block";
            continue;
        }
        allItems[i].style.display = "none";
    }
}