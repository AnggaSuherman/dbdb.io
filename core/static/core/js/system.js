(function ($){
    $('.markdown-area').each(function () {
       var text = $.trim($(this).text());
       var md = markdown.toHTML(text);
       $(this).html(md);
    });
    $.get('/update-view-count/');
    $('[data-toggle="popover"]').popover({'html': true});
}(jQuery));
