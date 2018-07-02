
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
	alert(myImput.value);
}
