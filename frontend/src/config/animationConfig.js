export const ANIMATION_VARIANTS = {
  hidden: { opacity: 0, y: 20 },
  visible: { 
    opacity: 1, 
    y: 0, 
    transition: { duration: 0.5, ease: 'easeOut' } 
  },
  hover: { scale: 1.02, transition: { duration: 0.2 } }
};

export const SCROLL_TRIGGER_OPTIONS = {
  threshold: 0.1,
  once: true
};
