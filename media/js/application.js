$(document).ready(function() {

    $.each($('.count'), function() {
        $(this).countTo({
            interval:    20,
            startNumber: 0,
            endNumber:   parseInt($(this).text()),
        });
    });

});

