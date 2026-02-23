// Register ScrollTrigger plugin
gsap.registerPlugin(ScrollTrigger);

// Initial page load animations
window.addEventListener('load', () => {
    // Animate navigation
    gsap.from('.nav-container', {
        y: -100,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
        delay: 0.2
    });

    // Animate hero elements - Staggered entrance
    gsap.from('.hero-title', {
        y: 100,
        opacity: 0,
        duration: 1.2,
        ease: 'power3.out',
        delay: 0.5
    });

    gsap.from('.hero-subtitle', {
        y: 50,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
        delay: 0.8
    });

    gsap.from('.hero-cta', {
        y: 30,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out',
        delay: 1
    });

    // Hero background parallax effect
    gsap.to('.hero-section', {
        backgroundPosition: '50% 100%',
        ease: 'none',
        scrollTrigger: {
            trigger: '.hero-section',
            start: 'top top',
            end: 'bottom top',
            scrub: true
        }
    });

    initScrollAnimations();
});

// Scroll-triggered animations
function initScrollAnimations() {
    // Section title animations
    gsap.utils.toArray('.section-title').forEach(title => {
        gsap.from(title, {
            scrollTrigger: {
                trigger: title,
                start: 'top 80%',
                toggleActions: 'play none none reverse'
            },
            y: 60,
            opacity: 0,
            duration: 1,
            ease: 'power3.out'
        });
    });

    // Feature cards stagger animation
    gsap.from('.feature-card', {
        scrollTrigger: {
            trigger: '.features-grid',
            start: 'top 80%',
            toggleActions: 'play none none reverse'
        },
        y: 80,
        opacity: 0,
        duration: 0.8,
        stagger: 0.2,
        ease: 'power3.out'
    });

    // Feature icons bounce effect
    gsap.from('.feature-icon', {
        scrollTrigger: {
            trigger: '.features-grid',
            start: 'top 80%'
        },
        scale: 0,
        opacity: 0,
        duration: 0.6,
        stagger: 0.15,
        ease: 'back.out(1.7)'
    });

    // About section animations
    gsap.from('.about-text', {
        scrollTrigger: {
            trigger: '.about-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        x: -80,
        opacity: 0,
        duration: 1,
        ease: 'power3.out'
    });

    gsap.from('.about-image', {
        scrollTrigger: {
            trigger: '.about-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        x: 80,
        opacity: 0,
        duration: 1,
        ease: 'power3.out'
    });

    // About statistics counter animation
    gsap.utils.toArray('.stat').forEach(stat => {
        gsap.from(stat, {
            scrollTrigger: {
                trigger: stat,
                start: 'top 85%'
            },
            scale: 0,
            opacity: 0,
            duration: 0.6,
            ease: 'elastic.out(1, 0.5)'
        });
    });

    // Contact form animations
    gsap.from('.contact-form', {
        scrollTrigger: {
            trigger: '.contact-section',
            start: 'top 70%',
            toggleActions: 'play none none reverse'
        },
        y: 60,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out'
    });

    gsap.from('.form-input, .form-textarea', {
        scrollTrigger: {
            trigger: '.contact-form',
            start: 'top 70%'
        },
        y: 30,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out'
    });

    gsap.from('.form-submit', {
        scrollTrigger: {
            trigger: '.contact-form',
            start: 'top 70%'
        },
        scale: 0.8,
        opacity: 0,
        duration: 0.5,
        delay: 0.4,
        ease: 'back.out(1.7)'
    });

    // Footer reveal animation
    gsap.from('.footer', {
        scrollTrigger: {
            trigger: '.footer',
            start: 'top 95%'
        },
        opacity: 0,
        duration: 0.8
    });
}
