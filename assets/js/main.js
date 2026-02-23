document.addEventListener('DOMContentLoaded', function() {
    console.log('App loaded');
    initApp();
});

function initApp() {
    const btn = document.querySelector('.btn');
    if (btn) {
        btn.addEventListener('click', handleClick);
    }
}

function handleClick(e) {
    e.preventDefault();
    alert('Clicked!');
}
