$(document).ready(function () {
	//button to get string from form
	$("#submit").click(function(){

	});

	//when enter is hit, dont refrsh the page.
	// instead, ...
	$("form").on('submit', function(event){

	});
});

/* Special thanks to Pratyush Chandra for this function. He posted it to his blog for anyone to use! */
/*                 It's awesome code that allows for you to store JSON directly into an object!              */
/*                                               Go check out his blog!                                                            */
/*                                 http://pratyush-chandra.blogspot.com/                                                    */
/*                                       The code can be found here:                                                            */
/*             http://pratyush-chandra.blogspot.com/2012/04/store-ajax-json-response-into.html          */
function getJson(url) {
	return JSON.parse($.ajax({
		type: 'GET',
		url: url,
		dataType: 'json',
		global: false,
		async:false,
		success: function(data) {
			return data;
		}
	}).responseText);
}