$('document').ready(function () {
  $('input#btn_translate').on('click', function () {
    const language = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${language}`;
    $.get(url, function (translation) {
      $('div#hello').text(translation?.hello);
    });
  });
});
