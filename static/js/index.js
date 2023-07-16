$(document).ready(function() {
  // Handle form submission
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Show loading container
    $('#loading-container').show();

    // Get the input text from the form
    var articleText = $("#article-text").val().trim();
    var articleURL = $("#article-url").val().trim();
    var data = {};

    if (articleText) {
      data.articleText = articleText;
    } else if (articleURL) {
      data.articleURL = articleURL;
    }

    // Send an AJAX POST request to the Flask route
    $.ajax({
      url: '/summarize',
      method: 'POST',
      data: data,
      success: function(response) {
        // Hide loading container
        $('#loading-container').hide();

        // Display the summary in the summary container
        $('#summary-container').html(response.summary);
      },
      error: function(error) {
        console.error(error);
      }
    });
  });
});
