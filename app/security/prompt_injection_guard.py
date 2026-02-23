import re

BLOCKLIST = [
    r"ignore (all )?(previous|above) instructions",
    r"system( prompt)?",
    r"override (your )?programming",
    r"jailbreak",
    r"act as (a )?unrestricted",
    r"respond as (a )?developer"
]

def validate_prompt(user_text):
    if not isinstance(user_text, str):
        return False
    text_lower = user_text.lower()
    for pattern in BLOCKLIST:
        if re.search(pattern, text_lower):
            return False
    return True
