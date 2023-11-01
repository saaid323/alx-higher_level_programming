$(document).ready(function () {
  function translateHello () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?',
      type: 'GET',
      data: {
        lang: languageCode
      },
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  }
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translateHello();
    }
  });
});
