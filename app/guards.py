import re

# Detect common prompt injection patterns
INJECTION_PATTERNS = [
    r'ignore (previous|all) instructions',
    r'print (system )?prompt',
    r'developer mode',
    r'act as (a )?jailbreak',
    r'dan 10\.0'
]

def sanitize_input(user_input: str) -> tuple[bool, str]:
    """Validates input for injection attempts. Returns (is_safe, reason)."""
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, f"Blocked by pattern: {pattern}"
    return True, "OK"

def sanitize_output(ai_response: str) -> str:
    """Redacts PII from AI output."""
    # Simple email/ssn redaction for demo
    response = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[REDACTED_EMAIL]', ai_response)
    response = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[REDACTED_SSN]', response)
    return response
