// Main application logic
function init() {
    console.log('App initialized');
    document.addEventListener('DOMContentLoaded', function() {
        loadContent();
    });
}

function loadContent() {
    const container = document.querySelector('.container');
    if (container) {
        container.innerHTML = '<p>Content loaded</p>';
    }
}

init();
