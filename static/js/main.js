// ------------- DETECTING TAB CHANGES---------------------


$("#resized").hide()
$("#switchTab1").hide()
$("#switchTab2").hide()
$("#switchTab3").hide()
$("#autoSubmit").hide()


var warn = 0

$(window).blur(function () {
    msg = ""
    warn++;
    if (warn == 1) {

        $(".switchTab1").show()
        $("#switchTab1").fadeTo(2000, 500).slideUp(500, function () {
            $("#switchTab1").slideUp(500);
        });

    }
    if (warn == 2) {

        $(".switchTab2").show()
        $("#switchTab2").fadeTo(5000, 500).slideUp(500, function () {
            $("#switchTab2").slideUp(500);
        });

    }
    if (warn == 3) {
        $(".switchTab3").show()
        $("#switchTab3").fadeTo(20000, 500).slideUp(500, function () {
            $("#switchTab3").slideUp(500);
        });
    }

    if (warn > 3) {
        $(".switchTab1").hide();
        $(".switchTab2").hide();
        $(".switchTab3").hide();
        $(".autoSubmit").show()
        $("#autoSubmit").fadeTo(20000, 500).slideUp(500, function () {
            $("#autoSubmit").slideUp(500);
        });
        setTimeout(function () {
            $(location).attr('href', window.location.origin + "/submit")
        }, 5000);

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
