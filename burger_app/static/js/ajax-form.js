$(function() {
    // Get the form.
    var form = $('#contact-form');

    // Get the messages div.
    var formMessages = $('.ajax-response');

    // Set up an event listener for the contact form.
    $(form).submit(function(e) {
        // Stop the browser from submitting the form.
        e.preventDefault();

        // Disable the submit button to prevent multiple submissions
        var submitButton = $(this).find('input[type="submit"]');
        submitButton.prop('disabled', true);

        // Serialize the form data.
        var formData = $(form).serialize();
        var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();

        // Submit the form using AJAX.
        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData,
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .done(function(response) {
            $(formMessages).removeClass('error').addClass('success');
            $(formMessages).text(response);
            $('#contact-form input,#contact-form textarea').val('');
        })
        .fail(function(data) {
            $(formMessages).removeClass('success').addClass('error');
            if (data.responseText !== '') {
                $(formMessages).text(data.responseText);
            } else {
                $(formMessages).text('Oops! An error occurred and your message could not be sent.');
            }
        })
        .always(function() {
            // Re-enable the submit button
            submitButton.prop('disabled', false);
        });
    });
});
