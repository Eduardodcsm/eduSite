// Simple example to toggle the visibility of the sidebar:
const sidebar = document.querySelector('aside');
const toggleButton = document.createElement('button');
toggleButton.textContent = 'Toggle Sidebar';

toggleButton.addEventListener('click', () => {
  sidebar.classList.toggle('hidden'); // Applies or removes the 'hidden' class
});

document.body.appendChild(toggleButton); // Adds the button to the body
