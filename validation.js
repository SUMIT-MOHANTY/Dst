document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const messageInput = document.getElementById('message');

    function validateName() {
        const value = nameInput.value.trim();
        const errorSpan = document.getElementById('nameError');
        if (value === '') {
            showError(nameInput, errorSpan, 'Name is required');
            return false;
        } else if (value.length < 2) {
            showError(nameInput, errorSpan, 'Name must be at least 2 characters');
            return false;
        } else {
            showValid(nameInput, errorSpan);
            return true;
        }
    }

    function validateEmail() {
        const value = emailInput.value.trim();
        const errorSpan = document.getElementById('emailError');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (value === '') {
            showError(emailInput, errorSpan, 'Email is required');
            return false;
        } else if (!emailRegex.test(value)) {
            showError(emailInput, errorSpan, 'Please enter a valid email');
            return false;
        } else {
            showValid(emailInput, errorSpan);
            return true;
        }
    }

    function validatePhone() {
        const value = phoneInput.value.trim();
        const errorSpan = document.getElementById('phoneError');
        const phoneRegex = /^[\d\s\-\(\)+]{10,}$/;
        if (value !== '' && !phoneRegex.test(value)) {
            showError(phoneInput, errorSpan, 'Please enter a valid phone number');
            return false;
        } else {
            showValid(phoneInput, errorSpan);
            return true;
        }
    }

    function validateMessage() {
        const value = messageInput.value.trim();
        const errorSpan = document.getElementById('messageError');
        if (value === '') {
            showError(messageInput, errorSpan, 'Message is required');
            return false;
        } else if (value.length < 10) {
            showError(messageInput, errorSpan, 'Message must be at least 10 characters');
            return false;
        } else {
            showValid(messageInput, errorSpan);
            return true;
        }
    }

    function showError(input, errorSpan, message) {
        input.classList.remove('valid');
        input.classList.add('invalid');
        errorSpan.textContent = message;
    }

    function showValid(input, errorSpan) {
        input.classList.remove('invalid');
        input.classList.add('valid');
        errorSpan.textContent = '';
    }

    nameInput.addEventListener('input', validateName);
    nameInput.addEventListener('blur', validateName);
    emailInput.addEventListener('input', validateEmail);
    emailInput.addEventListener('blur', validateEmail);
    phoneInput.addEventListener('input', validatePhone);
    phoneInput.addEventListener('blur', validatePhone);
    messageInput.addEventListener('input', validateMessage);
    messageInput.addEventListener('blur', validateMessage);

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const isNameValid = validateName();
        const isEmailValid = validateEmail();
        const isPhoneValid = validatePhone();
        const isMessageValid = validateMessage();

        if (isNameValid && isEmailValid && isPhoneValid && isMessageValid) {
            alert('Form submitted successfully!');
            form.reset();
            [nameInput, emailInput, phoneInput, messageInput].forEach(input => {
                input.classList.remove('valid');
            });
        }
    });
});
