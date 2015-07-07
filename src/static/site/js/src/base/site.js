$(document).ready(function() {
    // update card title
    var namedisplay_elm = $('#card_name_display');
    $(document).on('input', 'form', function() {
        if (this.elements.title.value == '')
            namedisplay_elm.html('15 Minutes of Daily Meditation');
        else
            namedisplay_elm.html(this.elements.title.value);
    });


    // draw 49 days card preview
    var card_draw_elm = $('#card_days_display');
    for (var i = 0; i < 21; i ++) {
        card_draw_elm.append($('<div></div>')
            .addClass('aday')
        );
    }

});
