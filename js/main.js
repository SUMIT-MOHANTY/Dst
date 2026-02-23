// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });

// Button hover animations added via JS for dynamic effects
document.querySelectorAll('.hero-cta, .form-submit').forEach(button => {
    button.addEventListener('mouseenter', () => {
        gsap.to(button, {
            scale: 1.05,
            duration: 0.3,
            ease: 'power2.out'
        });
    });

    button.addEventListener('mouseleave', () => {
        gsap.to(button, {
            scale: 1,
            duration: 0.3,
            ease: 'power2.out'
        });
    });

    button.addEventListener('click', (e) => {
        if (button.classList.contains('hero-cta')) {
            e.preventDefault();
            gsap.to(button, {
                scale: 0.95,
                duration: 0.1,
                yoyo: true,
                repeat: 1
            });
        }
    });
});

// Feature cards hover effect
document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        gsap.to(card, {
            y: -10,
            boxShadow: '0 20px 40px rgba(99, 102, 241, 0.2)',
            duration: 0.3,
            ease: 'power2.out'
        });
    });

    card.addEventListener('mouseleave', () => {
        gsap.to(card, {
            y: 0,
            boxShadow: '0 4px 6px rgba(0, 0, 0, 0.05)',
            duration: 0.3,
            ease: 'power2.out'
        });
    });
});

// Form input focus animations
document.querySelectorAll('.form-input, .form-textarea').forEach(input => {
    input.addEventListener('focus', () => {
        gsap.to(input, {
            borderColor: '#6366f1',
            boxShadow: '0 0 0 3px rgba(99, 102, 241, 0.2)',
            duration: 0.3
        });
    });

    input.addEventListener('blur', () => {
        gsap.to(input, {
            borderColor: 'rgba(255, 255, 255, 0.2)',
            boxShadow: '0 0 0 0 rgba(99, 102, 241, 0)',
            duration: 0.3
        });
    });
});

// Parallax effect on scroll for feature cards
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    document.querySelectorAll('.feature-card').forEach((card, index) => {
        const speed = 0.02 * (index + 1);
        gsap.to(card, {
            y: scrolled * speed,
            duration: 0.5,
            ease: 'none'
        });
    });
});

// Refresh ScrollTrigger on window resize
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        ScrollTrigger.refresh();
    }, 200);
});

console.log('Animation site loaded successfully! 🎬');
