import requests
import sys

def check_link(url):
    try:
        # Allow internal links or specific safe domains only
        if url.startswith('#') or url.startswith('/'):
            return True
        # Logic to check external links against an allowlist would go here
        # For this example, we just check connectivity
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code < 400
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

if __name__ == "__main__":
    print("Link validation utility initialized.")
