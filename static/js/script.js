// Contact form submission
document.getElementById('contact-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
    };
    const res = await fetch('/submit-contact', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    const result = await res.json();
    if (result.success) {
        document.getElementById('contact-form').classList.add('hidden');
        document.getElementById('success-message').classList.remove('hidden');
    }
});

// Scroll animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in-scroll').forEach(el => observer.observe(el));

// Check admin access
document.querySelector('a[href="/admin"]')?.addEventListener('click', async (e) => {
    e.preventDefault();
    const res = await fetch('/admin');
    if (!res.redirected) {
        document.getElementById('admin-modal').classList.remove('hidden');
    } else {
        window.location.href = '/admin';
    }
});

function closeModal() {
    document.getElementById('admin-modal').classList.add('hidden');
}

async function adminLogin() {
    const password = document.getElementById('admin-password').value;
    const res = await fetch('/admin-login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({password})
    });
    const result = await res.json();
    if (result.success) {
        window.location.href = '/admin';
    } else {
        alert('Invalid password');
    }
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
