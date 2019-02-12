// Navbar Dropdown hover
$('ul.navbar-nav li.dropdown').hover(
  function() {
    $(this)
      .find('.dropdown-menu')
      .stop(true, true)
      .delay(200)
      .fadeIn(500);
  },
  function() {
    $(this)
      .find('.dropdown-menu')
      .stop(true, true)
      .delay(200)
      .fadeOut(500);
  }
);

// Toggler details / specification
$('a#analysis').click(function() {
  $(this)
    .removeClass('btn-default')
    .addClass('btn-success');
  $('a#specification')
    .removeClass('btn-success')
    .addClass('btn-default');
  $('#analysis-content').addClass('active');
  $('#specification-content').removeClass('active');
});
$('a#specification').click(function() {
  $(this)
    .removeClass('btn-default')
    .addClass('btn-success');
  $('a#analysis')
    .removeClass('btn-success')
    .addClass('btn-default');
  $('#specification-content').addClass('active');
  $('#analysis-content').removeClass('active');
});
