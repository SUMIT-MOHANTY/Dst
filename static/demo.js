window.addEventListener('error', function(e) {
  console.warn('Asset failed, loading fallback:', e.message);
  document.body.classList.add('safe-mode');
});

function safeAnimate(element) {
  try {
    element.classList.add('animate-in');
  } catch (err) {
    element.style.opacity = '1'; // Fallback visibility
  }
}
