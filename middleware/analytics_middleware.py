from flask import request, g
from config.analytics_config import ANALYTICS_CONFIG

class AnalyticsMiddleware:
    def __init__(self, app):
        self.app = app
        app.before_request(self.before_request)
    
    def before_request(self):
        g.analytics_consent = False
        
        # Check for opt-out via DNT header
        if request.headers.get('DNT') == '1' and ANALYTICS_CONFIG['respect_dnt']:
            g.analytics_consent = False
            return
        
        # Check cookie consent
        consent_cookie = request.cookies.get('analytics_consent')
        g.analytics_consent = consent_cookie == 'granted'
        
        # Block analytics on sensitive paths
        path = request.path
        for blocked in ANALYTICS_CONFIG['blocked_paths']:
            if path.startswith(blocked):
                g.analytics_consent = False
                break
