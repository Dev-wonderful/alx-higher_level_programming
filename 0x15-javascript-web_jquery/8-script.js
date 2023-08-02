const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (films) {
  for (const film of films.results) {
    $('ul#list_movies').append($('<li></li>').text(film.title));
  }
});
