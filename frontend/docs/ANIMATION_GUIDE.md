# Animation Usage Guide

## Risks Mitigated
1. **Accessibility**: Always use `ScrollReveal` which respects `prefers-reduced-motion`.
2. **Performance**: Heavy libraries are chunked. `will-change` is applied via CSS.
3. **Consistency**: Durations and easings are centralized in `animationConfig.js`.

## Implementation
- Import `ScrollReveal` for scroll sections.
- Avoid arbitrary `style={{ animation }}` props.
- Test with Chrome DevTools > Rendering > Emulate reduced motion.
