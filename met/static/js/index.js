$(document).ready(function() {
  $(".scale-cell").hover(function() {
    var price = $(this).find(".scale-cell-price").html();
    var income = $(this).find(".scale-cell-income").html();
    $("#annotation-price").html(price.trim())
    $("#annotation-income").html(income.trim())
  }, function() {
    $("#annotation-price").html("____")
    $("#annotation-income").html("____")
  })
  
  const subscribe_url = '/subscribe';
  const subscribe_form = $(".subscribe-form");
  const subscribe_feedback_selector = '.subscribe-form-feedback';
  const subscribe_submit_selector = '.subscribe-form-submit';

  subscribe_newsletter(
          subscribe_url, 
          subscribe_form, 
          subscribe_feedback_selector,
          subscribe_submit_selector);
});

$(window).resize(function() {
});
