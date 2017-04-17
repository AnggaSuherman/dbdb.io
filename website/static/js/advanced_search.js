
NEXT_SELECTOR = {
  "icon-maybe": "icon-yes",
  "icon-yes": "icon-no",
  "icon-no": "icon-maybe"
};

NEXT_IMAGE = {
  "icon-maybe": "/static/images/icon-yes.png",
  "icon-yes": "/static/images/icon-no.png",
  "icon-no": "/static/images/icon-maybe.png"
};

$(document).ready(function() {
  $(".field-selector").click(function() {
    var curr_check = $(this).attr("data-current-check");
    $(this).removeClass(curr_check);
    $(this).addClass(NEXT_SELECTOR[curr_check]);
    $(this).attr("data-current-check", NEXT_SELECTOR[curr_check]);
    $(this).attr("src", NEXT_IMAGE[curr_check])
  });
  $(".search-button").click(function() {
    var results = {};
    $(".field-selector").each(function(i) {
      var field = $(this).attr("data-field");
      var check = $(this).attr("data-current-check");
      results[field] = check;
    });
    urlReq = "/" + "advancedsearch?" + jQuery.param(results);
    document.location.href = urlReq;
  })
});