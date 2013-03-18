$(document).ready(function() {

    $('.count').each(function() {
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

    $('#tweet_good .tweet_hidden').each(function() {
        var tweet = $(this);
        var timeout = Math.floor(Math.random()*4000) + 1000 * $(this).data('order');
        if ($(this).data('order') == 1) {
            timeout = 1200;
        }
        setTimeout(function() {
            $('#tweet_good').prepend(tweet);
            tweet.addClass('tweet_link').fadeIn().css("display","inline-block");
        }, timeout);
    });

    $('#tweet_bad .tweet_hidden').each(function() {
        var tweet = $(this);
        var timeout = Math.floor((Math.random()*5000)+1000) * ($(this).data('order')+1);
        if ($(this).data('order') == 1) {
            timeout = 2500;
        }
        setTimeout(function() {
            $('#tweet_bad').prepend(tweet);
            tweet.addClass('tweet_link').fadeIn().css("display","inline-block");
        }, timeout);
    });

    $('.tweet .details .text').each(function() {
        $(this).html($(this).html().replace(/faithinhumanity/gi, '<span class="faith">$&</span>'));
        $(this).html($(this).html().replace(/faith in humanity/gi, '<span class="faith">$&</span>'));
    })

});

