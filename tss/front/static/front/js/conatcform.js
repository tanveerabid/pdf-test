
$body = $("body");

$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }    
});

(function ($) {

    $('#submit').on('click', () => {
        event.preventDefault();
         $('.error').text('');
         $('.success').text('');
        const name = $('#name').val();
        const email = $('#email').val();
        const phone = $('#phone').val();
        const subject = $('#subject').val();
        const message = $('#message').val();
        if (name && email) {
            sendquery(name, email, phone, subject, message);
        }
        else{
            $('.error').text('Name & Email is required');
        }
    });

     $('#subscribe').on('click', () => {
        event.preventDefault();
         $('.subsuccess').text('');
        const email = $('#subscribe-email').val();
        if (email){
            sendsubscribe(email); 
        }
        else{
            $('.subsuccess').text('Email is required');
            $('.subsuccess').css("color", "Red");
        }
    });

    $('#clear').on('click', () => {
        event.preventDefault();
            $('#name').val(' ');
            $('#email').val(' ');
            $('#phone').val(' ');
            $('#subject').val(' ');
            $('#message').val(' ');
    });


})(jQuery);

const sendquery = function(name, email, phone, subject, message) {

    var formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('phone', phone);
    formData.append('subject', subject);
    formData.append('message', message);


    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/submitquery/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            if (res.res_code == 1) {
            $('.success').text(res.msg);
            $('#name').val(' ');
            $('#email').val(' ');
            $('#phone').val(' ');
            $('#subject').val(' ');
            $('#message').val(' ');
            }
            else{
            $('.error').text(res.msg);
            }
            
        }
    });
};




const sendsubscribe = function(email) {

    var formData = new FormData();
    formData.append('email', email);

    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/subscribe/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            if (res.res_code == 1) {
            $('.subsuccess').text(res.msg);
             $('.subsuccess').css("color", "Green");
            $('#subscribe-email').val(' ');
            }
            else{
            $('.subsuccess').text(res.msg);
            $('.subsuccess').css("color", "Red");
            }
            
        }
    });
};



