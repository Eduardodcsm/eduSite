// Data for tools and their descriptions
const toolsData = [
  { name: "GitHub", description: "GitHub was used for version control and collaboration." },
  { name: "Visual Studio Code", description: "Visual Studio Code was used to edit and organize files like HTML, CSS, and JavaScript." },
  { name: "Python", description: "Python was used for scripting and backend development." },
  { name: "HTML", description: "HTML was used for structuring the content of web pages." },
  { name: "CSS", description: "CSS was used for styling the web pages." },
  { name: "JavaScript", description: "JavaScript was used for client-side scripting and interactivity." },
  { name: "Java", description: "Java was used for backend development and application logic." },
  { name: "SQL", description: "SQL was used for database management and querying." }
];

// Function to display information based on the selected tool
function toggleSkillsList() {
  const skillsList = document.getElementById("tool-usage-display");
  const isVisible = skillsList.style.display === "block";

  if (!isVisible) {
    const listHTML = "<ul>" + toolsData.map(tool => `<li data-tool="${tool.name}">${tool.name}</li>`).join("") + "</ul>";
    skillsList.innerHTML = listHTML;
    skillsList.style.display = "block"; // Show the list

    skillsList.addEventListener("click", handleToolClick);
  } else {
    skillsList.style.display = "none"; // Hide the list
    skillsList.removeEventListener("click", handleToolClick);
  }
}

// Function to handle click event on tool items
function handleToolClick(event) {
  if (event.target.tagName === "LI") {
    const toolName = event.target.dataset.tool;
    const toolInfoDisplay = document.getElementById("tool-usage-display");
    const tool = toolsData.find(tool => tool.name === toolName);
    const message = tool ? tool.description : "Usage information not available.";

    toolInfoDisplay.innerHTML = "<p>" + message + "</p>";
    toolInfoDisplay.style.display = "block"; // Make the info display visible
  }
}
