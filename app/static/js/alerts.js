function confirmar(url){
    $.confirm({
        title: 'Confirmar ação',
        content: 'Deseja mesmo executar essa ação?',
        autoClose: 'CANCELAR|5000',
        buttons: {
            SIM:{
                keys: ['enter'],
                btnClass: 'btn-green',
                action: function(){
                    $.ajax({
                        url: url,
                        success: function () {
                            location.reload();
                        }
                      });
                }
            },
            CANCELAR:{
                keys: ['esc'],
                btnClass: 'btn-red any-other-class'
            }
        }
    });
}
