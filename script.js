// Data definition
const skillsData = [
    { name: 'Python', level: 90, icon: '🐍' },
    { name: 'JavaScript', level: 85, icon: '⚡' },
    { name: 'AI & ML', level: 75, icon: '🤖' }
];

// Mitigation for Security: Sanitize HTML to prevent XSS
function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

function renderSkills() {
    const container = document.getElementById('skills-container');
    
    // Clear container to prevent duplicate accumulation on re-runs
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    skillsData.forEach(skill => {
        // Mitigation: Use createElement/textContent instead of innerHTML
        const card = document.createElement('div');
        card.className = 'skill-card';
        card.setAttribute('role', 'listitem');

        const header = document.createElement('div');
        header.className = 'skill-header';

        const title = document.createElement('span');
        title.textContent = `${skill.icon} ${escapeHtml(skill.name)}`;
        
        const percent = document.createElement('span');
        percent.textContent = `${skill.level}%`;

        header.appendChild(title);
        header.appendChild(percent);

        const barContainer = document.createElement('div');
        barContainer.className = 'bar-container';

        const barFill = document.createElement('div');
        barFill.className = 'bar-fill';
        // Set CSS variable for fallback in reduced motion
        barFill.style.setProperty('--final-width', `${skill.level}%`);
        
        barContainer.appendChild(barFill);
        card.appendChild(header);
        card.appendChild(barContainer);
        container.appendChild(card);

        // Mitigation for Performance: Use requestAnimationFrame for smooth UI
        requestAnimationFrame(() => {
            // Small delay to ensure DOM insertion before transition
            setTimeout(() => {
                barFill.style.width = `${skill.level}%`;
            }, 50);
        });
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', renderSkills);
