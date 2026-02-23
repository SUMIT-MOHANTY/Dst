// Main application entry point
document.addEventListener('DOMContentLoaded', function() {
    console.log('App initialized');
    
    function init() {
        const btn = document.querySelector('button');
        if (btn) {
            btn.addEventListener('click', handleClick);
        }
    }
    
    function handleClick(e) {
        e.preventDefault();
        alert('Hello World!');
    }
    
    init();
});
