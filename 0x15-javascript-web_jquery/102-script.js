$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?',
      type: 'GET',
      data: {
        lang: lang
      },
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  });
});
