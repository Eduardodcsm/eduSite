// Function to display skills information
function showInfo(skill) {
    // Get reference to information display areas
    var pythonInfoDisplay = document.getElementById("python-infoDisplay");
    var webDevInfoDisplay = document.getElementById("web-dev-infoDisplay");
  
    // Display information based on the selected skill
    switch (skill) {
      case "Python":
        pythonInfoDisplay.innerHTML = "Python information: ...";
        webDevInfoDisplay.innerHTML = "";
        break;
      case "Flask":
        pythonInfoDisplay.innerHTML = "Flask information: ...";
        webDevInfoDisplay.innerHTML = "";
        break;
      case "HTML":
        pythonInfoDisplay.innerHTML = "";
        webDevInfoDisplay.innerHTML = "HTML was used to create and structure the content of the website. It facilitated the creation of 4 pages.";
        break;
      case "JavaScript":
        pythonInfoDisplay.innerHTML = "";
        webDevInfoDisplay.innerHTML = "JavaScript enabled functionalities such as the contact form and gallery, allowing users to interact with the website.";
        break;
      case "CSS":
        pythonInfoDisplay.innerHTML = "";
        webDevInfoDisplay.innerHTML = "CSS was applied for styling and layout, enhancing the visual appeal and user experience of the website.";
        break;
      case "Github":
        pythonInfoDisplay.innerHTML = "";
        webDevInfoDisplay.innerHTML = "GitHub was used for hosting the website, version control, and documentation purposes.";
        break;
      default:
        // Handle unknown skill
        pythonInfoDisplay.innerHTML = "Information not available for this skill.";
        webDevInfoDisplay.innerHTML = "";
        break;
    }
  }
  