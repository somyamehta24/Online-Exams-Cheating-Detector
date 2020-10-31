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
        $(".switchTab1").hide()
        $(".switchTab2").show()
        $("#switchTab2").fadeTo(5000, 500).slideUp(500, function () {
            $("#switchTab2").slideUp(500);
        });

    }
    if (warn == 3) {
        $(".switchTab1").hide()
        $(".switchTab2").hide()
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
            console.log("Button clicked")
            $("#submitButton").click()

        }, 5000);

    }

});



// -----------------------------------------------------------

$(window).on('resize', function () {
    $(".container").hide()
    $(".resized").show()
    $("#resized").fadeTo(20000, 500).slideUp(500, function () {
        $("#resized").slideUp(500);
    });
    setInterval(function () {
        $(".container").show()

    }, 1000)

});


// Disable copy paste
$(document).ready(function () {
    $('.form-group').on("cut copy paste", function (e) {
        e.preventDefault();
        alert("Copy paste detected")
    });
});


function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0;
            $(".switchTab1").hide();
            $(".switchTab2").hide();
            $(".switchTab3").hide();
            $(".autoSubmit").show()
            $("#autoSubmit").fadeTo(2000, 500).slideUp(500, function () {
                $("#autoSubmit").slideUp(500);
                $(location).attr('href', window.location.origin + "/submit")

            });



        }
    }, 1000);
}

window.onload = function () {
    var starting = 60 * 60,
        display = document.querySelector('#time');
    startTimer(starting, display);
};

