import bleach

def sanitize_string(input_data):
    if not input_data:
        return ""
    # Remove all HTML tags to prevent Stored XSS
    return bleach.clean(input_data, tags=[], strip=True)
