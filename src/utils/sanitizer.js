export function sanitizeInput(str) {
  const temp = document.createElement('div');
  temp.textContent = str;
  return temp.innerHTML;
}
