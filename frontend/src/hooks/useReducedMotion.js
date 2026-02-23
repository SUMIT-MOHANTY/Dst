import { useEffect, useState } from 'react';

export const useReducedMotion = () => {
  const [matches, setMatch] = useState(false);
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setMatch(mediaQuery.matches);
    const handler = (event) => setMatch(event.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);
  return matches;
};
