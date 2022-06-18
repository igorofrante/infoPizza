function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function totalPedido(){
  ls = ["p", "b"];
  valor = 0.0;
  for (let id = 0; id < 2; id++) {
    for (let index = 0;index < $("#id_form" + ls[id] + "-TOTAL_FORMS").val(); index++) {
        if ($("#id_form" + ls[id] +"-" + index + "-preco").val() != '' && $("#id_form" + ls[id] +"-" + index + "-DELETE").is(':checked')== false ){
          console.log($("#id_form" + ls[id] +"-" + index + "-preco").val())
          valor += parseFloat($("#id_form" + ls[id] + "-"+ index + "-preco").val());
        }
    }
  }
  $('#totalPedido').val(valor)


}

function ajaxe() {
  ls = ["p", "b"];
  for (let id = 0; id < 2; id++) {
    for (let index = 0;index < $("#id_form" + ls[id] + "-TOTAL_FORMS").val(); index++) {
      $("#id_form" + ls[id] + "-" + index + "-DELETE").change(totalPedido);
      $("#id_form" + ls[id] + "-" + index + "-produto").change(function () {
        var url = "/pedido/ajax/tamanhos";
        var produtoID = $(this).val();

        $("#id_form" + ls[id] + "-" + index + "-tamanho").val("");
        $("#id_form" + ls[id] + "-" + index + "-preco").val("");

        $.ajax({
          url: url,
          data: {
            produto: produtoID,
          },
          success: function (data) {
            $("#id_form" + ls[id] + "-" + index + "-tamanho").html(data);
          },
        });
      });

      $("#id_form" + ls[id] + "-" + index + "-tamanho").change(function () {
        var url = "/pedido/ajax/preco";
        var tamanhoID = $(this).val();

        $.ajax({
          url: url,
          data: {
            tamanho: tamanhoID,
          },
          success: function (data) {
            $("#id_form" + ls[id] + "-" + index + "-preco").val(data);
            totalPedido();
          },
        });
      });
      
    }
  }
}
function ajaxe2() {
  ls = ["p", "b"];
  for (let id = 0; id < 2; id++) {
    for (
      let index = 0;
      index < $("#id_form" + ls[id] + "-TOTAL_FORMS").val();
      index++
    ) {
      $(function () {
        var url = "/pedido/ajax/tamanhos2";
        var produtoID = $("#id_form" + ls[id] + "-" + index + "-produto").val();

        if (produtoID != "") {
          $.ajax({
            url: url,
            data: {
              produto: produtoID,
            },
            success: function (data) {
              $("#id_form" + ls[id] + "-" + index + "-tamanho").html(data);
            },
          });
          sleep(100);
          var url = "/pedido/ajax/tamanho";
          var idx = $("#id_form" + ls[id] + "-" + index + "-id").val();
          $.ajax({
            url: url,
            data: {
              idx: idx,
            },
            success: function (data) {
              $(
                "#id_form" +
                  ls[id] +
                  "-" +
                  index +
                  "-tamanho option[value=" +
                  data +
                  "]"
              ).attr("selected", "selected");
            },
          });
        }
      });
    }
  }
}

$(document).ready(function(){
    ajaxe();
    ajaxe2();
    totalPedido();


    $("#addPizza").click(function (ev) {
        ev.preventDefault();
        var count = $(".pizzas").children().length;
        var tmplMarkup = $("#pizza-" + (count - 1)).html();
        var compiledTmpl = tmplMarkup.replaceAll(count - 1, count);
        var dyv = "<div id=pizza-" + count + ">subs</div>";
        var dyv = dyv.replace("subs", compiledTmpl);
        $(".pizzas").append(dyv);
      
        // update form count
        $("#id_formp-TOTAL_FORMS").attr("value", count + 1);
      
        // some animate to scroll to view our new form
        $("html, body").animate(
          {
            scrollTop: $("#addPizza").position().top - 200,
          },
          800
        );
        ajaxe();
      });
      
      $("#addBebida").click(function (ev) {
        ev.preventDefault();
        var count = $(".bebidas").children().length;
        var tmplMarkup = $("#bebida-" + (count - 1)).html();
        var compiledTmpl = tmplMarkup.replaceAll(count - 1, count);
        var dyv = "<div id=bebida-" + count + ">subs</div>";
        var dyv = dyv.replace("subs", compiledTmpl);
        $(".bebidas").append(dyv);
      
        // update form count
        $("#id_formb-TOTAL_FORMS").attr("value", count + 1);
      
        // some animate to scroll to view our new form
        $("html, body").animate(
          {
            scrollTop: $("#addPizza").position().top - 200,
          },
          800
        );
        ajaxe();
      });
});


