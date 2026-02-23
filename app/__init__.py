from .guards import sanitize_input, sanitize_output

def process_request(user_query):
    safe, reason = sanitize_input(user_query)
    if not safe:
        return f"Security Alert: {reason}"
    return "AI Processed Response"
