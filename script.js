// Function to display information based on the clicked skill
function showInfo(skill) {
    var infoDisplay = document.getElementById('infoDisplay');
  
    // Clear previous content
    infoDisplay.innerHTML = '';
  
    // Display information based on the clicked skill
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
      // Add more cases for additional skills
    }
  }
  