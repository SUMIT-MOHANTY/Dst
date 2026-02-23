import bleach
import re

def sanitize_html_input(raw_input):
    if not raw_input: return ""
    tags = []
    attrs = {}
    return bleach.clean(raw_input, tags=tags, attributes=attrs, strip=True)

def sanitize_sql_keywords(raw_input):
    pattern = r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|EXEC|ALTER|TRUNCATE)\b)"
    if re.search(pattern, raw_input, re.IGNORECASE):
        raise ValueError("SQL Injection pattern detected.")
    return raw_input
