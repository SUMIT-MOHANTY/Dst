document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const successMessage = document.getElementById('success-message');

    const validators = {
        name: { required: true, minLength: 2, pattern: /^[a-zA-Z\s]+$/ },
        email: { required: true, pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
        phone: { pattern: /^[+]?[\d\s\-()]{10,}$/ },
        subject: { required: true },
        message: { required: true, minLength: 10 }
    };

    const errorMessages = {
        name: {
            required: 'Name is required',
            minLength: 'Name must be at least 2 characters',
            pattern: 'Name can only contain letters'
        },
        email: {
            required: 'Email is required',
            pattern: 'Please enter a valid email address'
        },
        phone: {
            pattern: 'Please enter a valid phone number (min 10 digits)'
        },
        subject: {
            required: 'Please select a subject'
        },
        message: {
            required: 'Message is required',
            minLength: 'Message must be at least 10 characters'
        }
    };

    function validateField(field) {
        const value = field.value.trim();
        const fieldName = field.name;
        const rules = validators[fieldName];
        const errorElement = document.getElementById(`${fieldName}-error`);
        let isValid = true;
        let errorMessage = '';

        if (rules.required && value === '') {
            isValid = false;
            errorMessage = errorMessages[fieldName].required;
        } else if (rules.minLength && value.length < rules.minLength) {
            isValid = false;
            errorMessage = errorMessages[fieldName].minLength;
        } else if (rules.pattern && !rules.pattern.test(value) && value !== '') {
            isValid = false;
            errorMessage = errorMessages[fieldName].pattern;
        }

        field.classList.remove('valid', 'invalid');
        errorElement.textContent = '';

        if (value !== '' || rules.required) {
            if (isValid) {
                field.classList.add('valid');
            } else {
                field.classList.add('invalid');
                errorElement.textContent = errorMessage;
            }
        }

        return isValid;
    }

    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => {
            if (input.classList.contains('invalid')) {
                validateField(input);
            }
        });
    });

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        let isFormValid = true;

        inputs.forEach(input => {
            const result = validateField(input);
            if (!result) {
                isFormValid = false;
            }
        });

        if (isFormValid) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';

            setTimeout(() => {
                successMessage.classList.remove('hidden');
                form.reset();
                inputs.forEach(input => input.classList.remove('valid', 'invalid'));
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Message';

                setTimeout(() => {
                    successMessage.classList.add('hidden');
                }, 3000);
            }, 1500);
        } else {
            const firstInvalid = form.querySelector('.invalid');
            if (firstInvalid) {
                firstInvalid.focus();
            }
        }
    });
});