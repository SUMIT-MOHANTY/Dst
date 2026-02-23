document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const statusEl = document.getElementById('formStatus');
    statusEl.textContent = 'Sending...';
    statusEl.style.color = '#666';
    try {
        const response = await fetch('/contact', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        if (data.status === 'success') {
            statusEl.textContent = 'Message sent successfully!';
            statusEl.style.color = 'green';
            this.reset();
        }
    } catch (error) {
        statusEl.textContent = 'Error sending message.';
        statusEl.style.color = 'red';
    }
});
