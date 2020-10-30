// ------------- DETECTING TAB CHANGES ---------------------

// var warn = 0

// $(window).blur(function () {
//     msg = ""
//     warn++;
//     if (warn == 1) {

//         msg += "First Warning"
//     }
//     if (warn == 2) {

//         msg += "Second Warning"
//     }
//     if (warn == 3) {

//         msg += "Last Warning"
//     }

//     if (warn > 3)
//         msg = "Submitted"

//     alert(msg)
// });

// -----------------------------------------------------------

$(window).on('resize', function () {
    $(".container").hide()
    alert("Please do not resize the page")
});

$(document).ready(function () {
    $('.form-group').on("cut copy paste", function (e) {
        e.preventDefault();
    });
});

