function confirmar(event,tipo){
    texto = "";
    switch (tipo) {
        case 1:
            texto = "Deseja excluir esse dado?"
            break;
        case 2:
            texto = "Deseja cancelar este pedido?"
            break;
        case 3:
            texto = "Deseja liberar esta mesa?"
            break;
        default:
            break;
    }
    if(!confirm(texto)){
        event.preventDefault();
    }
 }

 

// function confirmar(event,tipo){
//     bol = false;
//     $.confirm({
//         title: 'Confirmar ação',
//         content: 'Deseja mesmo executar essa ação?',
//         autoClose: 'CANCELAR|5000',
//         buttons: {
//             SIM:{
//                 keys: ['enter'],
//                 btnClass: 'btn-green',
//                 action: function(){
//                     bol = true;
//                 }
//             },
//             CANCELAR:{
//                 keys: ['esc'],
//                 btnClass: 'btn-red any-other-class',
//                 action: function(){
//                     bol = false;
//                 }
//             }
//         }
//     });

//    if (!bol){
//     event.preventDefault();
//    }
// }
