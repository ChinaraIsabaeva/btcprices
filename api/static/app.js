$(document).ready(function(){
    $('.panel-title').click(function(){
        $('i').toggleClass('fa-caret-right fa-caret-down');
    });

    var bigJSONObject = [
        {
            date: "20 Nov 2015 16:00:04",
            kraken: "322.41",
            bitfinex: "322.05",
            bitstamp: "322.05",
            okcoin: "322.18"
        }
    ];

    $.each($('.response').children(), function(idx, child) {
        $(child).text(JSON.stringify(bigJSONObject, null, 4));
    });
});