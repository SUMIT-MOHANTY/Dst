import DOMPurify from 'dompurify';

export const sanitizeHTML = (html) => {
  if (typeof window === 'undefined') return html;
  return DOMPurify.sanitize(html);
};
