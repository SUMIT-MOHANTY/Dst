CSP_DIRECTIVES = {
    "default-src": "'self'",
    "script-src": "'self' 'unsafe-inline' localhost",
    "style-src": "'self' 'unsafe-inline'",
    "img-src": "'self' data: https:
}

def apply_csp_headers(response):
    """Helper to inject security headers during testing"""
    policy = "; ".join([f"{k} {v}" for k, v in CSP_DIRECTIVES.items()])
    response.headers["Content-Security-Policy"] = policy
