var interval = 0.5;    //Time between the msgs.
var count = 50;        //Number of times msg has to be send.
var message = "Hi";    //Msg that has to be sent.
var i = 0;             //Variable initializing to zero.
var timer = setInterval(function()
{
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');	
	i++;
	if( i  == count )
	clearInterval(timer);
},
interval * 1000 );
