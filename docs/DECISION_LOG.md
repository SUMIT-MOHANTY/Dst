# Framework Finalization

## Choices
1. **CSS Framework**: Tailwind CSS
   - *Rationale*: Superior tree-shaking (removes unused CSS) resulting in smaller bundles than Bootstrap.
   - *Risk Mitigated*: Performance Degradation.
   
2. **Animation Library**: GSAP
   - *Rationale*: High performance engine, better control over complex sequences than AOS.
   - *Risk Mitigated*: Jank/Main thread blocking.

## Operational Safeguards
- Security headers configured.
- `prefers-reduced-motion` handling native to CSS and JS.
- NPM audit lock-step versioning.
