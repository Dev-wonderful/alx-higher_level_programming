$('document').ready(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').on('click', function () {
    const allItems = $('ul.my_list').children();
    const length = allItems.length;
    allItems[length - 1].remove();
  });
  $('div#clear_list').on('click', function () {
    $('ul.my_list').html('');
  });
});
