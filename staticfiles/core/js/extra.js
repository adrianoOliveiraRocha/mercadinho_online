
function test(){
	
}

function alterQuantity(element_id){

	td = document.getElementById(element_id);
	td.innerHTML = "<input name='"+element_id+"'> "+
	" <input type='button' value='Enviar' "+
	" onclick='redirectAQ("+element_id+");'>"; 
	
}

function redirectAQ(imputName) {
	myImput = document.getElementsByName(imputName)[0];
	orderitem = parseInt(myImput.name); //order item id
	quantity = parseInt(myImput.value); //new value for quantity
	url = '';
	if (isNaN(quantity)) {
		alert('Por favor! digite a quantidade');
	} else {
		url = '/area_do_cliente/update_value/' + orderitem + '/' + quantity;
		window.self.location.href = url;
	}
		
}
