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
