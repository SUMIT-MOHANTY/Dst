// Main application logic
document.addEventListener('DOMContentLoaded', function() {
    console.log('App loaded');
    
    function init() {
        const header = document.querySelector('h1');
        if (header) {
            header.addEventListener('click', function() {
                alert('Hello World!');
            });
        }
    }
    
    init();
});
