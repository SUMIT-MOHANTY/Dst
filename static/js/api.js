import { appStore } from './store.js';

let currentController = null;

export async function fetchData(endpoint) {
    // Risk Mitigation: Abort previous request to prevent race conditions
    if (currentController) {
        currentController.abort();
    }
    currentController = new AbortController();
    
    appStore.setLoading(true);
    
    try {
        const response = await fetch(endpoint, {
            method: 'GET',
            signal: currentController.signal,
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        
        const json = await response.json();
        appStore.setData(json.payload);
    } catch (err) {
        if (err.name !== 'AbortError') {
            appStore.setError(err.message);
        }
    } finally {
        appStore.setLoading(false);
        currentController = null;
    }
}
