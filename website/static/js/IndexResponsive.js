//For index, text is aligned to the first event item.

//Create "on resize" event listener. Runs func on screen resize
window.addEventListener('resize', () => changeMargin());

function changeMargin() {
    //Text to change margin
    var eventHeader = document.getElementById("UpcomingEventHeader");

    //Event items + container
    var firstItem = document.getElementById("firstEventItem");
    var mainBox = document.getElementById("mainBox");

    //Get positions
    var firstItemPos = firstItem.getBoundingClientRect();
    var mainBoxPos = mainBox.getBoundingClientRect();

    //Apply offset
    eventHeader.style.marginLeft = (firstItemPos.left - mainBoxPos.left - 15) + "px";
}

function pictoSelect(picto) {
    var pictos = document.getElementsByClassName("sportPicto");

    pictos[picto];
}