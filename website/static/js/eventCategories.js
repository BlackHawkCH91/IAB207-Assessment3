function SportCategories() {
    var enabled = [];

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
                enabledItems[i2].style.display = "block";
            }
        }

        return;
    }

    //Show everything if nothing is selected
    for (var i = 0; i < allItems.length; i++) {
        allItems[i].style.display = "block";
    }
}