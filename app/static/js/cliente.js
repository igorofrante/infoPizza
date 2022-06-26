$(document).ready(function (){
    $('#id_cpf').mask('000.000.000-00')
    $('#id_cep').mask('00000-000')
    $('#id_telefone_1').attr('placeholder','Telefone com DDD')

    $('#id_cep').change(function () {
        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');
    
        //Verifica se campo cep possui valor informado.
        if (cep != "") {
    
            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;
    
            //Valida o formato do CEP.
    
            $.getJSON('https://viacep.com.br/ws/'+cep+'/json/', function(data) {
            // JSON result in data variable
                $('#id_logradouro').val(data.logradouro)
                $('#id_bairro').val(data.bairro)
                $('#id_cidade').val(data.localidade)
                $('#id_cep').val(data.cep)
            });
        }
    })
})

