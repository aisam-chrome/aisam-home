$(function() {
  $('.btn').on('click', function(event) {
      event.preventDefault();
      $(this).toggleClass('active');
  });

  $('.btn').click(function() {
    $('.good').addclass('active');
  });
});