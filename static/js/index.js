$(document).ready(function() {
  // Handle form submission
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Show loading container
    $('#loading-container').show();

    // Get the input text from the form
    var inputText = $('#article-text').val() || $('#article-url').val();

    // Send an AJAX POST request to the Flask route
    $.ajax({
      url: '/summarize',
      method: 'POST',
      data: { input_text: inputText },
      success: function(response) {
        // Hide loading container
        $('#loading-container').hide();

        // Display the summary in a new div or element
        // Replace 'summary-container' with the appropriate container ID or selector
        $('#summary-container').html(response.summary);
      },
      error: function(error) {
        console.error(error);
      }
    });
  });
});

