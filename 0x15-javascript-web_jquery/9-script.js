$('document').ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (greeting) {
    $('div#hello').text(greeting.results[0].title);
  });
});
