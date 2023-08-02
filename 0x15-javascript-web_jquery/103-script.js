$('document').ready(function () {
  function translate () {
    const language = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${language}`;
    $.get(url, function (translation) {
      $('div#hello').text(translation?.hello);
    });
  }

  $('input#btn_translate').on('click', translate);
  $('input#language_code').keypress(function (event) {
    const key = event.which;
    if (key === 13) {
      translate();
    }
  });
});
