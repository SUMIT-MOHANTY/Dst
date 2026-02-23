function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;
    appendMessage(message, 'user');
    input.value = '';
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    }).then(r => r.json()).then(data => {
        appendMessage(data.reply, 'ai');
    });
}
function appendMessage(text, type) {
    const div = document.createElement('div');
    div.className = 'message ' + type + '-message';
    div.textContent = text;
    document.getElementById('chat-messages').appendChild(div);
}
document.getElementById('user-input').addEventListener('keypress', e => {
    if (e.key === 'Enter') sendMessage();
});
