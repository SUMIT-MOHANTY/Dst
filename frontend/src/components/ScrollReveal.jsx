import { motion } from 'framer-motion';
import { useReducedMotion } from '../hooks/useReducedMotion';
import { ANIMATION_VARIANTS } from '../config/animationConfig';

export const ScrollReveal = ({ children, className = '' }) => {
  const shouldReduceMotion = useReducedMotion();

  const variants = shouldReduceMotion 
    ? { hidden: { opacity: 1, y: 0 }, visible: { opacity: 1, y: 0 } }
    : ANIMATION_VARIANTS;

  return (
    <motion.section
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '-50px' }}
      variants={variants}
      className={className}
    >
      {children}
    </motion.section>
  );
};
