document.addEventListener('DOMContentLoaded', () => {
const form = document.getElementById('contactForm');
const feedback = document.getElementById('formFeedback');
const submitBtn = document.getElementById('submitBtn');
const HONEYPOT_FIELD = 'honeytrap_field';
const MIN_MESSAGE_LENGTH = 10;
const MAX_MESSAGE_LENGTH = 1000;
let lastSubmit = 0;
const RATE_LIMIT_MS = 3000; // 3 seconds cooldown

// HTML Entity Escaping to prevent XSS when echoing data
const escapeHtml = (unsafe) => {
return unsafe
.replace(/&/g, "&amp;")
.replace(/</g, "&lt;")
.replace(/>/g, "&gt;")
.replace(/"/g, "&quot;")
.replace(/'/g, "&#039;");
}

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const validateInput = (input, type) => {
const isEmpty = !input.value.trim();
const errorDiv = document.getElementById(`error-${input.id}`);

if (isEmpty) {
errorDiv.innerText = 'This field is required.';
return false;
}

if (type === 'email' && !emailRegex.test(input.value.toLowerCase())) {
errorDiv.innerText = 'Please enter a valid email address.';
return false;
}

if (type === 'message') {
const len = input.value.length;
if (len < MIN_MESSAGE_LENGTH) {
errorDiv.innerText = `Message must be at least ${MIN_MESSAGE_LENGTH} chars.`;
return false;
}
if (len > MAX_MESSAGE_LENGTH) {
errorDiv.innerText = `Message too long (max ${MAX_MESSAGE_LENGTH}).`;
return false;
}
}

errorDiv.innerText = '';
return true;
};

['input', 'blur'].forEach(evt => {
['name', 'email', 'message'].forEach(id => {
const el = document.getElementById(id);
if(el) el.addEventListener(evt, () => validateInput(el, id));
});
});

form.addEventListener('submit', async (e) => {
e.preventDefault();

// Honeytrap check (Anti-bot)
const honey = form.querySelector(`input[name="${HONEYPOT_FIELD}"]`);
if (honey && honey.value) {
console.warn('Bot detected via honeytrap');
return;
}

const now = Date.now();
if (now - lastSubmit < RATE_LIMIT_MS) {
feedback.innerText = 'Please wait a moment before submitting again.';
feedback.style.color = 'orange';
return;
}

const isNameValid = validateInput(document.getElementById('name'), 'text');
const isEmailValid = validateInput(document.getElementById('email'), 'email');
const isMsgValid = validateInput(document.getElementById('message'), 'message');

if (isNameValid && isEmailValid && isMsgValid) {
submitBtn.disabled = true;
submitBtn.innerText = 'Sending...';
lastSubmit = now;
feedback.innerText = '';

const formData = {
name: escapeHtml(document.getElementById('name').value.trim()),
email: escapeHtml(document.getElementById('email').value.trim()),
message: escapeHtml(document.getElementById('message').value.trim())
};

try {
// Placeholder for actual API endpoint
const response = await fetch('/api/contact/submit', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(formData)
});

if (response.ok) {
feedback.innerText = 'Message sent successfully!';
feedback.style.color = 'green';
form.reset();
} else {
throw new Error('Server response not OK');
}
} catch (err) {
console.error(err);
feedback.innerText = 'Failed to send message. Please try again later.';
feedback.style.color = 'red';
} finally {
submitBtn.disabled = false;
submitBtn.innerText = 'Send Message';
}
}
});
});
