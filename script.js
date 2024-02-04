document.addEventListener('DOMContentLoaded', function () {
  const { PythonShell } = require('python-shell');

  function showInfo(skill) {
    var infoDisplay = document.getElementById('infoDisplay');
    infoDisplay.innerHTML = '';

    switch (skill) {
      case 'HTML':
        infoDisplay.innerHTML = "Was used to create and structure the content of the website. Seated 4 pages using HTML.";
        break;
      case 'JavaScript':
        infoDisplay.innerHTML = "Was used to enable functionalities in the contact form and gallery, allowing the user to toggle the photographs.";
        break;
      case 'CSS':
        infoDisplay.innerHTML = "Was applied for styling and layout, enhancing the visual appeal of the website.";
        break;
    }
  }

  var infoDisplay = document.getElementById('infoDisplay');
  var loadingSpinner = '<div class="spinner"></div>'; // Add some CSS for a loading spinner

  // Show loading spinner while Python script is running
  infoDisplay.innerHTML = loadingSpinner;

  PythonShell.run('GUIbox.py', null, function (err, results) {
    if (err) throw err;

    console.log('Python script finished with output:', results);

    // Display the Python script's output on the HTML page
    infoDisplay.innerHTML = "<pre>" + results.join('\n') + "</pre>";
  });
});

function runPython() {
  // Use fetch to trigger a Flask route that runs the Python file
  fetch('/run_python')
      .then(response => response.json())
      .then(data => {
          console.log(data); // You can handle the response if needed
      })
      .catch(error => {
          console.error('Error:', error);
      });
}

  