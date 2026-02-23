document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const successMessage = document.getElementById('successMessage');
    const resetBtn = document.getElementById('resetBtn');
    const submitBtn = document.getElementById('submitBtn');
    const messageField = document.getElementById('message');
    const charCount = document.getElementById('charCount');
    
    const MAX_MESSAGE_LENGTH = 500;
    const MIN_MESSAGE_LENGTH = 10;
    
    const validators = {
        name: {
            validate: (value) => value.trim().length >= 2 && /^[a-zA-Z\s'-]+$/.test(value.trim()),
            error: 'Please enter a valid name (at least 2 characters, letters only)',
            required: true
        },
        email: {
            validate: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()),
            error: 'Please enter a valid email address',
            required: true
        },
        phone: {
            validate: (value) => value.trim() === '' || /^[\+\d\s\-()]{10,}$/.test(value.trim()),
            error: 'Please enter a valid phone number (at least 10 digits)',
            required: false
        },
        subject: {
            validate: (value) => value.trim() !== '',
            error: 'Please select a subject',
            required: true
        },
        message: {
            validate: (value) => value.trim().length >= MIN_MESSAGE_LENGTH && value.trim().length <= MAX_MESSAGE_LENGTH,
            error: `Message must be between ${MIN_MESSAGE_LENGTH} and ${MAX_MESSAGE_LENGTH} characters`,
            required: true
        }
    };
    
    function validateField(field) {
        const fieldId = field.id;
        const validator = validators[fieldId];
        
        if (!validator) return true;
        
        const value = field.value;
        const errorElement = document.getElementById(`${fieldId}Error`);
        
        let isValid = true;
        let errorMessage = '';
        
        if (validator.required && value.trim() === '') {
            isValid = false;
            errorMessage = 'This field is required';
        } else if (value.trim() !== '' && !validator.validate(value)) {
            isValid = false;
            errorMessage = validator.error;
        } else if (validator.required && !validator.validate(value)) {
            isValid = false;
            errorMessage = validator.error;
        }
        
        field.classList.remove('valid', 'invalid');
        errorElement.classList.remove('show');
        
        if (value.trim() !== '') {
            if (isValid) {
                field.classList.add('valid');
            } else {
                field.classList.add('invalid');
                errorElement.textContent = errorMessage;
                errorElement.classList.add('show');
            }
        }
        
        return isValid;
    }
    
    function validateAllFields() {
        const fields = form.querySelectorAll('input, select, textarea');
        let allValid = true;
        
        fields.forEach(field => {
            if (validators[field.id] && !validateField(field)) {
                allValid = false;
            }
        });
        
        return allValid;
    }
    
    function updateCharCount() {
        const length = messageField.value.length;
        const remaining = MAX_MESSAGE_LENGTH - length;
        
        charCount.textContent = `${length}/${MAX_MESSAGE_LENGTH}`;
        
        charCount.classList.remove('warning', 'error');
        
        if (remaining < 50 && remaining >= 0) {
            charCount.classList.add('warning');
        } else if (remaining < 0) {
            charCount.classList.add('error');
        }
        
        validateField(messageField);
    }
    
    function attachValidationListeners(field) {
        field.addEventListener('blur', () => validateField(field));
        field.addEventListener('input', () => {
            validateField(field);
            if (field.id === 'message') {
                updateCharCount();
            }
        });
    }
    
    const allFields = form.querySelectorAll('input, select, textarea');
    allFields.forEach(attachValidationListeners);
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (validateAllFields()) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';
            
            setTimeout(() => {
                form.classList.add('hidden');
                successMessage.classList.remove('hidden');
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Message';
            }, 1500);
        } else {
            submitBtn.classList.add('shake');
            setTimeout(() => submitBtn.classList.remove('shake'), 500);
        }
    });
    
    resetBtn.addEventListener('click', function() {
        form.reset();
        form.querySelectorAll('input, select, textarea').forEach(field => {
            field.classList.remove('valid', 'invalid');
            const errorElement = document.getElementById(`${field.id}Error`);
            if (errorElement) {
                errorElement.classList.remove('show');
            }
        });
        charCount.textContent = '0/500';
        charCount.classList.remove('warning', 'error');
        successMessage.classList.add('hidden');
        form.classList.remove('hidden');
    });
    
    updateCharCount();
});