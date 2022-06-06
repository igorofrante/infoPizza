(function(win,doc){
    'use strict';

    //Verifica se o usuário realmente quer deletar o dado
    if(doc.querySelector('.bi-trash3')){
        let btnDel = doc.querySelectorAll('.bi-trash3');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
})(window,document);

