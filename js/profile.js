const profileData = {
    name: 'Nitesh Saw',
    title: 'Full Stack Developer & Technology Enthusiast',
    initials: 'NS',
    bio: 'Passionate about building innovative solutions and pushing the boundaries of technology. With expertise in modern web development and a keen eye for design, I transform complex problems into elegant user experiences. I believe in writing clean, maintainable code and staying updated with the latest industry trends.',
    socials: [
        { platform: 'GitHub', url: 'https://github.com/niteshsaw', icon: 'GH' },
        { platform: 'LinkedIn', url: 'https://linkedin.com/in/niteshsaw', icon: 'LI' },
        { platform: 'Twitter', url: 'https://twitter.com/niteshsaw', icon: 'TW' },
        { platform: 'Email', url: 'mailto:nitesh@saw.dev', icon: 'EM' }
    ],
    background: [
        {
            date: '2022 - Present',
            title: 'Senior Software Engineer',
            organization: 'Tech Innovation Labs',
            description: 'Leading development of scalable web applications and mentoring junior developers.'
        },
        {
            date: '2020 - 2022',
            title: 'Full Stack Developer',
            organization: 'Digital Solutions Inc',
            description: 'Developed and maintained multiple client-facing applications using React and Node.js.'
        },
        {
            date: '2018 - 2020',
            title: 'Junior Developer',
            organization: 'StartUp Vision',
            description: 'Started career building responsive web interfaces and learning modern development practices.'
        }
    ],
    skills: ['JavaScript', 'Python', 'React', 'Node.js', 'TypeScript', 'PostgreSQL', 'Docker', 'AWS', 'Git', 'REST APIs', 'GraphQL', 'Agile'],
    contact: {
        location: 'San Francisco, CA',
        email: 'nitesh@saw.dev',
        website: 'niteshsaw.dev',
        availability: 'Open to opportunities'
    }
};

function renderProfile() {
    document.getElementById('profile-name').textContent = profileData.name;
    document.getElementById('profile-title').textContent = profileData.title;
    document.getElementById('profile-avatar').textContent = profileData.initials;
    document.getElementById('profile-bio').textContent = profileData.bio;
    
    const socialLinks = document.getElementById('social-links');
    profileData.socials.forEach(social => {
        const link = document.createElement('a');
        link.href = social.url;
        link.className = 'social-link';
        link.target = '_blank';
        link.innerHTML = `<span>${social.icon}</span><span>${social.platform}</span>`;
        socialLinks.appendChild(link);
    });
    
    const timeline = document.getElementById('background-timeline');
    profileData.background.forEach(item => {
        const timelineItem = document.createElement('div');
        timelineItem.className = 'timeline-item';
        timelineItem.innerHTML = `
            <div class="timeline-date">${item.date}</div>
            <div class="timeline-title">${item.title}</div>
            <div class="timeline-organization">${item.organization}</div>
            <div class="timeline-description">${item.description}</div>
        `;
        timeline.appendChild(timelineItem);
    });
    
    const skillsContainer = document.getElementById('skills-container');
    profileData.skills.forEach(skill => {
        const badge = document.createElement('span');
        badge.className = 'badge';
        badge.textContent = skill;
        skillsContainer.appendChild(badge);
    });
    
    const contactInfo = document.getElementById('contact-info');
    const contactItems = [
        { label: 'Location', value: profileData.contact.location },
        { label: 'Email', value: profileData.contact.email },
        { label: 'Website', value: profileData.contact.website },
        { label: 'Status', value: profileData.contact.availability, class: 'success' }
    ];
    contactItems.forEach(item => {
        const contactItem = document.createElement('div');
        contactItem.className = 'contact-item';
        contactItem.innerHTML = `
            <span class="contact-label">${item.label}:</span>
            <span class="contact-value">${item.value}</span>
        `;
        contactInfo.appendChild(contactItem);
    });
}

document.addEventListener('DOMContentLoaded', renderProfile);
