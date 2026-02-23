(function() {
    const TRACKING_ID = 'UA-XXXXXXXXX-X';
    const API_ENDPOINT = '/api/analytics/event';
    
    function sendEvent(category, action, label) {
        const payload = {
            category: category,
            action: action,
            label: label,
            path: window.location.pathname,
            userAgent: navigator.userAgent.substring(0, 100),
            timestamp: Date.now()
        };
        navigator.sendBeacon(API_ENDPOINT, JSON.stringify(payload));
    }
    
    function trackPageView() {
        sendEvent('pageview', 'load', window.location.pathname);
    }
    
    if (document.readyState === 'complete') {
        trackPageView();
    } else {
        window.addEventListener('load', trackPageView);
    }
    
    window.analytics = { sendEvent };
})();
