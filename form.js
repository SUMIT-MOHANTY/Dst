document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const subjectInput = document.getElementById('subject');
    const messageInput = document.getElementById('message');
    const submitBtn = document.querySelector('.submit-btn');
    const successMessage = document.getElementById('successMessage');

    const patterns = {
        name: /^[a-zA-Z\s]{2,50}$/,
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phone: /^\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$/
    };

    function validateField(input, pattern, optional = false) {
        const formGroup = input.closest('.form-group');
        const value = input.value.trim();
        
        if (optional && value === '') {
            formGroup.classList.remove('error', 'success');
            return true;
        }
        
        if (pattern && pattern.test(value) || (!pattern && value.length >= 10)) {
            formGroup.classList.remove('error');
            formGroup.classList.add('success');
            return true;
        } else {
            formGroup.classList.remove('success');
            formGroup.classList.add('error');
            return false;
        }
    }

    function validateForm() {
        let isValid = true;
        isValid &= validateField(nameInput, patterns.name);
        isValid &= validateField(emailInput, patterns.email);
        isValid &= validateField(phoneInput, patterns.phone, true);
        isValid &= validateField(subjectInput, null);
        isValid &= validateField(messageInput, null);
        return isValid;
    }

    function setSubmitting(isSubmitting) {
        submitBtn.disabled = isSubmitting;
        submitBtn.classList.toggle('loading', isSubmitting);
    }

    function showSuccess() {
        form.classList.add('hidden');
        successMessage.classList.remove('hidden');
        setTimeout(() => {
            successMessage.classList.add('show');
        }, 10);
    }

    function resetForm() {
        form.reset();
        document.querySelectorAll('.form-group').forEach(group => {
            group.classList.remove('error', 'success');
        });
        form.classList.remove('hidden');
        successMessage.classList.remove('show');
        successMessage.classList.add('hidden');
        setSubmitting(false);
    }

    nameInput.addEventListener('blur', () => validateField(nameInput, patterns.name));
    emailInput.addEventListener('blur', () => validateField(emailInput, patterns.email));
    phoneInput.addEventListener('blur', () => validateField(phoneInput, patterns.phone, true));
    subjectInput.addEventListener('change', () => validateField(subjectInput, null));
    messageInput.addEventListener('blur', () => validateField(messageInput, null));

    nameInput.addEventListener('input', function() {
        if (this.closest('.form-group').classList.contains('error')) {
            validateField(nameInput, patterns.name);
        }
    });

    phoneInput.addEventListener('input', function() {
        let value = this.value.replace(/\D/g, '');
        if (value.length >= 6) {
            value = `(${value.slice(0,3)}) ${value.slice(3,6)}-${value.slice(6,10)}`;
        } else if (value.length >= 3) {
            value = `(${value.slice(0,3)}) ${value.slice(3)}`;
        } else if (value.length > 0) {
            value = `(${value}`;
        }
        this.value = value;
    });

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (validateForm()) {
            setSubmitting(true);
            
            setTimeout(() => {
                showSuccess();
                setTimeout(resetForm, 4000);
            }, 1500);
        } else {
            const firstError = document.querySelector('.form-group.error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                firstError.querySelector('input, select, textarea').focus();
            }
        }
    });
});
