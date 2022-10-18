//On input value change event
function rating() {
    var inputs = document.getElementsByClassName("ratingRadio");
    var labels = document.getElementsByClassName("ratingLabel");
    var radioValue = 0;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            break;
        }
        radioValue++;
    }

    for (var i = 0; i < labels.length; i++) {
        if (radioValue >= 0) {
            labels[i].style.color = "orange";
            radioValue--;
        } else {
            labels[i].style.color = "#212529";
        }
    }
}

function rating2() {
    var inputs = document.getElementsByClassName("ratingRadio2");
    var labels = document.getElementsByClassName("ratingLabel2");
    var radioValue = 0;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            break;
        }
        radioValue++;
    }

    for (var i = 0; i < labels.length; i++) {
        if (radioValue >= 0) {
            labels[i].style.color = "orange";
            radioValue--;
        } else {
            labels[i].style.color = "#212529";
        }
    }
}