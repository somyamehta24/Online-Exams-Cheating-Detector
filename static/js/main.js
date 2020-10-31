// ------------- DETECTING TAB CHANGES---------------------


$(".resized").hide()
$(".switchTab").hide()
var warn = 0

$(window).blur(function () {
    msg = ""
    warn++;
    if (warn == 1) {

        $(".switchTab").show()

    }
    if (warn == 2) {

        $(".switchTab").show()

    }
    if (warn == 3) {
        $(".switchTab").show()
    }

    if (warn > 3) {
        msg = "Submitted"
        alert(msg)

        warn = -1000
        $(".container").hide()
        $(location).attr('href', window.location.origin + "/submit")


    }

});

// -----------------------------------------------------------

$(window).on('resize', function () {
    $(".container").hide()
    $(".resized").show()

});


// Disable copy paste
$(document).ready(function () {
    $('.form-group').on("cut copy paste", function (e) {
        e.preventDefault();
        alert("Copy paste detected")
    });
});

