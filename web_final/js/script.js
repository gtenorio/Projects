$(document).ready(function() {
    $('.btnTop').hover(function(){
        if($(this).children().attr('class') == "fa fa-envelope fa-fw"){
            $(this).animate({width: '+=70px'}, 100);
        }
        else if($(this).children().attr('class') == "fa fa-facebook fa-fw"){
            $(this).animate({width: '+=110px'}, 100);
        }
        else{
            $(this).animate({width: '+=100px'}, 100);
        }
    },function(){
        if($(this).children().attr('class') == "fa fa-envelope fa-fw"){
            $(this).animate({width: '-=70px'}, 100);
        }
        else if($(this).children().attr('class') == "fa fa-facebook fa-fw"){
            $(this).animate({width: '-=110px'}, 100);
        }
        else{
            $(this).animate({width: '-=100px'}, 100);
        }
    });

});

$(function($){
    var addToAll = false;
    var gallery = true;
    var titlePosition = 'inside';
    $(addToAll ? 'img' : 'img.fancybox').each(function(){
        var $this = $(this);
        var title = $this.attr('title');
        var src = $this.attr('data-big') || $this.attr('src');
        var a = $('<a href="#" class="fancybox"></a>').attr('href', src).attr('title', title);
        $this.wrap(a);
    });
    if (gallery)
        $('a.fancybox').attr('rel', 'fancyboxgallery');
    $('a.fancybox').fancybox({
        titlePosition: titlePosition
    });
});
$.noConflict();
