function delivery(order_id, opt){
	var url = '/area_do_cliente/delivery/' + order_id + '/' + opt;
	window.self.location.href = url;
}

function solicitation(opt){
	let element = document.getElementById("solicitation").style.visibility = "visible" ;
	if (opt === 1) {
		document.getElementById("solicitation").style.visibility = "visible" ;
		document.getElementById("btn_solicitation").style.visibility = "hidden" ;
	} else {
		document.getElementById("solicitation").style.visibility = "hidden";
		document.getElementById("btn_solicitation").style.visibility = "visible";
	}
}

