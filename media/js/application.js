$(document).ready(function() {

    $.each($('.count'), function() {
        $(this).countTo({
            interval:    20,
            startNumber: 0,
            endNumber:   parseInt($(this).text()),
        });
    });

    var good_bar = $("#thermometer #good");
    var bad_bar = $("#thermometer #bad");

    good_bar.css('width', 940 * good_bar.data('percentage') / 100 + 'px');
    bad_bar.css('width', 940 * bad_bar.data('percentage') / 100 + 'px');

    setTimeout(function() {
        if (good_bar.data('percentage') == 100) {
            good_bar.css({
               "border-radius": "10px",
               "-moz-border-radius": "10px",
               "-webkit-border-radius": "10px"
            });
        }

        if (bad_bar.data('percentage') == 100) {
            bad_bar.css({
               "border-radius": "10px",
               "-moz-border-radius": "10px",
               "-webkit-border-radius": "10px"
            });
        }
    }, 900);

});

