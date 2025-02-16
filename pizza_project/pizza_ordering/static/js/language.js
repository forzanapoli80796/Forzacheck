// language.js

// Function to switch language
function switchLanguage(language) {
    localStorage.setItem('preferredLanguage', language); // Save language preference to localStorage
    var elements = document.querySelectorAll('[data-lang-en]');
    elements.forEach(function(element) {
        element.innerText = element.getAttribute('data-lang-' + language);
    });
    // Update placeholders for input fields (if needed)
    document.getElementById('name').placeholder = language === 'en' ? 'Enter your name' : 'Geben Sie Ihren Namen ein';
    // Update button text (if needed)
    document.querySelector('input[type="submit"]').value = language === 'en' ? 'Submit' : 'Einreichen';
    // Update home button text (if needed)
    document.querySelector('.home-button').innerText = language === 'en' ? 'Home' : 'Startseite';
}

// Initialize placeholders and set language based on saved preference
document.addEventListener('DOMContentLoaded', function() {
    var savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    switchLanguage(savedLanguage); // Apply language on page load
});
