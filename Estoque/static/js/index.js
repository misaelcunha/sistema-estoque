//Alerta
setTimeout(() => {
    document.querySelector('#alerta').style.display = 'none';
}, 3000)

//Confirmação ao deletar
function confirmDeletion(event){
    if (!confirm('O material será deletado, tem certeza?')){
        event.preventDefault();
    }
}