document.addEventListener('DOMContentLoaded', () => {
const links = document.querySelectorAll('a[target="_blank"]');
links.forEach(link => {
if (!link.rel.includes('noopener')) {
console.warn('Security Risk: External link missing rel="noopener"', link.href);
link.setAttribute('rel', 'noopener noreferrer');
}
});
const images = document.querySelectorAll('img');
images.forEach(img => {
if (!img.alt) {
console.error('Accessibility Error: Image missing alt text', img.src);
img.alt = 'Project image';
}
});
console.log('Project Grid Initialized. Security scan complete.');
});