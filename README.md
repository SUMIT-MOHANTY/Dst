# GSAP Animated Website

A complete website implementation with smooth GSAP-powered entrance animations.

## Features

- **Smooth Page Load Animations**: Hero elements animate in with staggered timing
- **Scroll-Triggered Animations**: Sections reveal as you scroll down
- **Hover Effects**: Interactive animations on buttons and cards
- **Responsive Design**: Works seamlessly on all screen sizes
- **Performance Optimized**: Uses GSAP's optimized animation engine

## Sections

1. **Navigation**: Smooth slide-in animation on page load
2. **Hero Section**: Staggered entrance animations for title, subtitle, and CTA
3. **Features**: Cards animate in with stagger and bounce effects
4. **About**: Slide-in animations for text and image elements
5. **Contact**: Form elements animate on scroll with focus effects
6. **Footer**: Fade-in animation at bottom

## Animation Types Used

- `gsap.from()`: Entrance animations starting from a state
- `gsap.to()`: Animations to a target state
- `stagger`: Sequential animation delays for grouped elements
- `ScrollTrigger`: Animations triggered by scroll position
- `ease: 'power3.out'`: Smooth easing for natural motion
- `ease: 'back.out(1.7)'`: Bouncy elastic effect

## How to Use

Simply open `index.html` in a web browser. No build process required.

## Dependencies

- GSAP 3.12.2 (loaded via CDN)
- ScrollTrigger Plugin (loaded via CDN)

## Customization

Edit `js/animations.js` to modify animation timings, easing, and effects.
Edit `css/style.css` to change colors and styling.
