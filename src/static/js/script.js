// Theme toggle functionality
const themeToggleBtn = document.getElementById('theme-toggle-btn');
const appLogos = document.querySelectorAll('.app-logo');

// Toggle between light and dark themes
themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    // Update logos based on the active theme
    const isDarkTheme = document.body.classList.contains('dark-theme');
    appLogos.forEach((logo) => {
        const newLogo = isDarkTheme
            ? logo.getAttribute('data-dark-logo') // Use dark logo for dark theme
            : logo.getAttribute('data-light-logo'); // Use light logo for light theme
        logo.setAttribute('src', newLogo);
    });

    // Save theme preference to localStorage
    localStorage.setItem('theme', isDarkTheme ? 'dark' : 'light');
});

// Apply saved theme on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    const isDarkTheme = savedTheme === 'dark';

    if (isDarkTheme) {
        document.body.classList.add('dark-theme');
        document.body.classList.remove('light-theme');
    } else if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-theme');
    }

    // Set logos based on the saved theme
    appLogos.forEach((logo) => {
        const newLogo = isDarkTheme
            ? logo.getAttribute('data-dark-logo')
            : logo.getAttribute('data-light-logo');
        logo.setAttribute('src', newLogo);
    });
});
