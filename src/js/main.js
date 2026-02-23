import { sanitizeInput } from '../utils/sanitizer.js';
const projects = [
  { id: 1, title: 'Project Alpha', desc: 'A secure dashboard built with vanilla JS.', img: 'placeholder.jpg', link: '#' },
  { id: 2, title: 'Beta Analytics', desc: 'Real-time data processing unit.', img: 'placeholder.jpg', link: '#' },
  { id: 3, title: 'Gamma Cloud', desc: 'Scalable cloud infrastructure templates.', img: 'placeholder.jpg', link: '#' }
];
const grid = document.getElementById('project-grid');
if (grid) {
  projects.forEach(p => {
    const article = document.createElement('article');
    article.className = 'card';
    article.setAttribute('role', 'listitem');
    const safeTitle = sanitizeInput(p.title);
    const safeDesc = sanitizeInput(p.desc);
    article.innerHTML = `
      <img src='${p.img}' alt='${safeTitle} thumbnail' class='card-image' loading='lazy' />
      <div class='card-content'>
        <h2 class='card-title'>${safeTitle}</h2>
        <p class='card-desc'>${safeDesc}</p>
        <a href='${p.link}' class='card-link' aria-label='View details for ${safeTitle}'>View Details</a>
      </div>
    `;
    grid.appendChild(article);
  });
}
