// Function to display information based on the selected tool
function toggleSkillsList() {
  var skillsList = document.getElementById("tool-usage-display");
  var isVisible = skillsList.style.display === "block";

  if (!isVisible) {
    skillsList.innerHTML = `
      
      <ul>
        <li onclick="showInfo('GitHub')">GitHub</li>
        <li onclick="showInfo('Visual Studio Code')">Visual Studio Code</li>
        <li onclick="showInfo('Python')">Python</li>
        <li onclick="showInfo('HTML')">HTML</li>
        <li onclick="showInfo('CSS')">CSS</li>
        <li onclick="showInfo('JavaScript')">JavaScript</li>
        <li onclick="showInfo('Java')">Java</li>
        <li onclick="showInfo('SQL')">SQL</li>
      </ul>
    `;
    skillsList.style.display = "block"; // Show the list
  } else {
    skillsList.style.display = "none"; // Hide the list
  }
}

function showInfo(toolName) {
  var toolInfoDisplay = document.getElementById("tool-usage-display");
  var message;

  switch (toolName) {
    case "GitHub":
      message = "GitHub was used for version control and collaboration.";
      break;
    case "Visual Studio Code":
      message =
        "Visual Studio Code was used to edit and organize files like HTML, CSS, and JavaScript.";
      break;
    case "Python":
      message = "Python was used for scripting and backend development.";
      break;
    case "HTML":
      message = "HTML was used for structuring the content of web pages.";
      break;
    case "CSS":
      message = "CSS was used for styling the web pages.";
      break;
    case "JavaScript":
      message =
        "JavaScript was used for client-side scripting and interactivity.";
      break;
    case "Java":
      message = "Java was used for backend development and application logic.";
      break;
    case "SQL":
      message = "SQL was used for database management and querying.";
      break;
    default:
      message = "Usage information not available.";
  }

  toolInfoDisplay.innerHTML = "<p>" + message + "</p>";
  toolInfoDisplay.style.display = "block"; // Make the info display visible
}
