jQuery(document).ready(function() {

  var offset = 250;
  var duration = 300;
  jQuery(window).scroll(function() {
    if (jQuery(this).scrollTop() > offset) {
      jQuery(‘.back-to-top’).fadeIn(duration);
    } else {
      jQuery(‘.back-to-top’).fadeOut(duration);
    }
  });

  jQuery(‘.back-to-top’).click(function(event) {
    event.preventDefault();
    jQuery(‘html, body’).animate({scrollTop: 0}, duration);
    return false;
  })

});


jQuery(document).ready(function() {
  jQuery('.tabs .tab-links a').on('click', function(e)  {
    var currentAttrValue = jQuery(this).attr('href');
    // Show/Hide Tabs
    jQuery('.tabs ' + currentAttrValue).show().siblings().hide();
    // Change/remove current tab to active
    jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
    e.preventDefault();
  });
});
