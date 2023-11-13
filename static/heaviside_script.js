$(document).ready(function() {
    $('#heaviside-form').submit(function(event) {
        event.preventDefault();
        var xValue = $('#inputX').val();

        $.ajax({
            type: 'POST',
            url: '/calculate_heaviside',
            contentType: 'application/json',
            data: JSON.stringify({ 'x': parseFloat(xValue) }), // Parse float values
            success: function(response) {
                $('#result').html("Heaviside Function Result: " + response.result);
                $('#plot').html('<img src="data:image/png;base64,' + response.plot + '" />');
                // Set the results display to flex
                $('.results').css('display', 'flex');
            },
            error: function(xhr, status, error) {
                console.log(error); // Log any errors to the console for debugging
            }
        });
    });
});
