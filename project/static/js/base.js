var openMenu = false;
var page; 

$(document).ready(function(){

	page = get_current_page();
	
	if(page == "login" || page == "register") {
		$('.menu').remove();
		$('header').remove();
		$('content').css('top', '0', 'margin', '0', 'padding', '0', 'height', '100%')
	} else {
		$('content').height($('content').height()-50)
		$('.menu').height($('.menu').height()-50)
	}

	$('.toggleMenu').on('click', function(){
		if(!openMenu) {
			$('.menu').animate({width: "30%", opacity: "1"}, 50);
			$('content').animate({width: "70%"}, 50);
		} else {
			$('.menu').animate({width: "0", opacity: "0"}, 50);
			$('content').animate({width: "100%"}, 50);
		}
		openMenu = !openMenu;
	});

});

function get_current_page(){ 
	return window.location.pathname.split('/').pop()
}