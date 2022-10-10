function EditReview(x) {
    var review = document.getElementById("review");
    var edit = document.getElementById("edit");
    if (x == 1) {
        review.style.display = "none";
        edit.style.display = "block";
        return;
    }

    review.style.display = "block";
    edit.style.display = "none";
}