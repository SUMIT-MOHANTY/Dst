from flask import request, redirect, current_app

class HTTPSRedirectMiddleware:
    def __init__(self, app):
        self.app = app
        self.init_app(app)
    
    def init_app(self, app):
        app.before_request(self.force_https)
    
    def force_https(self):
        if not request.is_secure and current_app.config.get('SSL_REDIRECT'):
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)
        return None
