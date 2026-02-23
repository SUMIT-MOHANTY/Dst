document.addEventListener('DOMContentLoaded', function() {
    console.log('App loaded');
    const btn = document.querySelector('#btn');
    if(btn) {
        btn.addEventListener('click', () => {
            alert('Clicked!');
        });
    }
});
