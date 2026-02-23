import { fetchData } from './api.js';
import { appStore } from './store.js';
import { sanitize } from './utils.js';

// UI Component Logic
function render(state) {
    const container = document.getElementById('data-container');
    const status = document.getElementById('status');

    if (state.isLoading) {
        status.textContent = 'Loading...';
        return;
    }

    if (state.error) {
        status.textContent = 'Error: ' + sanitize(state.error);
        status.style.color = 'red';
        return;
    }

    status.textContent = 'Loaded';
    // Risk Mitigation: Use textContent or map through sanitized values to prevent XSS
    container.innerHTML = state.data.map(item => 
        `<li>${sanitize(item)}</li>`
    ).join('');
}

// Initialize
appStore.subscribe(render);

// Simulate asynchronous integration action
document.getElementById('load-btn').addEventListener('click', () => {
    fetchData('/api/data');
});
