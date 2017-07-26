(function (){
    'use strict';
    $(document).ready(function(){

       $('.like-message').click(function(){
       alert("Pressed a like button!");
       var request = $.ajax({
       url: "http://127.0.0.1:8000/like/",
       method: "POST",
       data: {id : "Sunt id"}
       });
       request.done(function (){

       alert("success!");
       });
       request.fail(function(){
       alert("FAILL!");
       });

       });

     $('.dislike-message').click(function(){
       alert("Pressed a dislike button!");
       });
       });

})();
