function safeUpdate(id, content) {
    const el = document.getElementById(id);
    if (el) {
        // Use textContent or strict validation to prevent XSS
        el.textContent = content;
        el.classList.add('fade-in');
    }
}
window.addEventListener('DOMContentLoaded', () => {
    const content = document.getElementById('app-content');
    if (window.innerWidth < 768) {
        content.style.gap = '10px';
    }
});
