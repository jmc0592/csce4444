$(document).ready(function () {
	//button to get string from form and call to riot api using function
	$("#submit").click(function(){
		var champ = document.getElementById("champ");
		$("#statdisplay").html("");
		var champresult = getChamp(champ.value)
		champ.value = "";
	});

	//when enter is hit, dont refrsh the page.
	// instead, get the string from the form and call to riot api using function
	$("form").on('submit', function(event){
		var champ = document.getElementById("champ");
		$("#statdisplay").html("");
		var champresult = getChamp(champ.value)
		champ.value = "";
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
		
		
function printChampion(champion){
	$("#statdisplay").append(champion.name+"<br>"+champion.title+
										"<br><br>Hitpoints: "+champion.stats.hp + "<br>Mana: "+champion.stats.mp+
										"<br>HP Regen per 5: "+champion.stats.hpregenperlevel+"<br>Mana Regen per 5: "+champion.stats.mpregenperlevel+
										"<br>Attack Damage: "+champion.stats.attackdamage+"<br>Ability Power: 0"+
										"<br>Attack Speed: "+getChampAttackspd(champion.stats.attackspeedoffset)+
										"<br>Attack Range: "+champion.stats.attackrange+"<br>Move Speed: "+champion.stats.movespeed+
										"<br><br><u>LORE</u><br>"+champion.lore);
}

function getChampAttackspd(offset){
	var ans = (.625/(1+offset));
	ans = ans.toFixed(2);
	return ans;
}