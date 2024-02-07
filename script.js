// script.js
// Function to show the content of skills
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
  // Add CSS class to the infoDisplay element
  infoDisplay.classList.add('infoDisplayStyle');
}


 
