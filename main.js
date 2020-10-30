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
    console.log("Resizing")
});

