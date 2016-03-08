$('#search_movies').click(function() { 

        $.ajax({
            url: 'controller/addBookmark',
            type: 'POST',
            data: {'query':true}, // An object with the key 'submit' and value 'true;
            success: function (result) {
              
            }
        });  

});