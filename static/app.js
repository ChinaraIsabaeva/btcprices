$(document).ready(function(){
    $('.panel-title').click(function(){
        $('i').toggleClass('fa-caret-right fa-caret-down');
    });

    var bigJSONObject = [
        {
	    bitfinex: "441.90",
	    btce: "434.80",
	    okcoin: "441.19",
	    kraken: "438.50",
	    coinbase: "440.89",
	    bitstamp: "438.02",
	    date: "20 Feb 2016 23:01:48"
	}
    ];

    $.each($('.response').children(), function(idx, child) {
        $(child).text(JSON.stringify(bigJSONObject, null, 2));
    });
});