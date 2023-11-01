$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (n) {
      for (let i = 0; i < n.results.length; i++) {
        const d = n.results[i];
        $('#list_movies').append('<li>' + d.title + '</li>');
      }
    }
  });
});
