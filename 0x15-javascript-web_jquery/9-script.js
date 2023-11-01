$(document).ready(function () {
  $(function () {
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      success: function (n) {
        $('#hello').text(n.hello);
      }
    });
  });
});
