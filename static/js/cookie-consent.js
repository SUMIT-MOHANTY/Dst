(function() {
    const CONSENT_KEY = 'analytics_consent';
    const BANNER_ID = 'cookie-banner';
    
    function init() {
        const consent = localStorage.getItem(CONSENT_KEY);
        const banner = document.getElementById(BANNER_ID);
        
        if (!consent) {
            banner.classList.remove('hidden');
        }
        
        document.getElementById('accept-cookies').addEventListener('click', function() {
            localStorage.setItem(CONSENT_KEY, 'granted');
            banner.classList.add('hidden');
            location.reload();
        });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
