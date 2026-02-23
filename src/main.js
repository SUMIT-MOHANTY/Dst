import { gsap } from 'gsap';

// Mitigation: Check for user preference before animating
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function initAnimations() {
  if (prefersReducedMotion) {
    console.log('Animations disabled for accessibility');
    document.body.classList.remove('opacity-0');
    return;
  }

  gsap.to('.hero-text', {
    duration: 1.2,
    y: 0,
    opacity: 1,
    ease: 'power3.out'
  });
}

window.addEventListener('load', initAnimations);
