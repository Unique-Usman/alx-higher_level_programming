$(document).ready(function () {
  $("#btn_translate").click(function() {
    let code = $("#language_code").val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, function (data, status){
      $("#hello").text(data.hello);
    })

    $("#language_code").focus(function () {
      $("body").keydown(function (e) {
        if (e.keyCode === 13) {
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, function (data, status){
          $("#hello").text(data.hello);
        })
        }
      })
    })
  })
});

