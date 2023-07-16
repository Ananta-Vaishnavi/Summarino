$(document).ready(function() {
  // Handle form submission
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Show loading container
    $('#loading-container').show();

    // Get the input text from the form
    var inputText = $('#article-text').val();

    // Send an AJAX POST request to the Flask route
    $.ajax({
      url: '/summarize',
      method: 'POST',
      data: { input_text: inputText },
      success: function(response) {
        // Hide loading container
        $('#loading-container').hide();

        // Display the summary in the summary container
        $('#summary-container').html(response);
      },
      error: function(error) {
        console.error(error);
      }
    });
  });
});

