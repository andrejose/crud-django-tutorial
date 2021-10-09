(function(win, doc){
	'use strict';

	// Confirmação para excluir um regitro
	if (doc.querySelector('.btn-delete')) {
		let btnDelete = doc.querySelectorAll('.btn-delete')
		for (let i=0; i < btnDelete.length; i++)
			btnDelete[i].addEventListener('click', function(event){
				if (confirm('Tem certeza que deseja excluir o registro?')) {
					return true;
				} else{
					event.preventDefault();
				}
			});
	}

	// Enviando a requisição por AJAX
	if (doc.querySelector('#form')) {
		let form = doc.querySelector('#form');

		function sendForm(event) {
			event.preventDefault();
			let data = new FormData(form);
			let ajax = new XMLHttpRequest();
			let token = doc.querySelectorAll('input')[0];
			ajax.open('POST', form.action);
			ajax.setRequestHeader('X-CSRF-TOKEN', token);
			ajax.onreadystatechange = function(){
				if (ajax.status == 200 && ajax. readyState == 4) {
					let result = doc.querySelector('#result');
					result.innerHTML = 'Operação realizada com sucesso!';
					result.classList.add('alert', 'alert-success');
				}
			}
			ajax.send(data);
			if (form.action.indexOf('update') == -1) form.reset();
		}

		form.addEventListener('submit', sendForm, false);
	}


})(window, document);