 // Function to show the content of skills
 function showInfo(skill) {
  var pythonInfoDisplay = document.getElementById("python-infoDisplay");
  var webDevInfoDisplay = document.getElementById("web-dev-infoDisplay");

  switch (skill) {
      case "Python":
          pythonInfoDisplay.innerHTML = "Python information goes here.";
          webDevInfoDisplay.innerHTML = "";
          break;
      case "Flask":
          pythonInfoDisplay.innerHTML = "Flask information goes here.";
          webDevInfoDisplay.innerHTML = "";
          break;
      case "HTML":
          pythonInfoDisplay.innerHTML = "teste";
          webDevInfoDisplay.innerHTML = "Was used to create and structure the content of the website. Seated 4 pages using HTML.";
          break;
      case "JavaScript":
          pythonInfoDisplay.innerHTML = "";
          webDevInfoDisplay.innerHTML = "Was used to enable functionalities in the contact form and gallery, allowing the user to toggle the photographs.";
          break;
      case "CSS":
          pythonInfoDisplay.innerHTML = "";
          webDevInfoDisplay.innerHTML = "Was applied for styling and layout, enhancing the visual appeal of the website.";
          break;
      case "Github":
          pythonInfoDisplay.innerHTML = "";
          webDevInfoDisplay.innerHTML = "Used to host the website, version control and documentation.";
          break;
  }
}