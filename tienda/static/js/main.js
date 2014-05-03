$(document).ready(function() {
      $("#preferences").click(function(event){
          $('#content').load('/preferences/');
      });
      $("#listado").click(function(event){
          $('#content').load('/listado/');
      });
      $("#calendario").click(function(event){
          $('#content').load('/calendario/');
      });
      $("#miembros").click(function(event){
          $('#content').load('/miembros/');
      });
   });


var jumboHeight = $('.jumbotron').outerHeight();
function parallax(){
    var scrolled = $(window).scrollTop();
    $('.bg').css('height', (jumboHeight-scrolled) + 'px');
}

$(window).scroll(function(e){
    parallax();
});