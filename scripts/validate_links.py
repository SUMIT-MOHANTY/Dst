import requests
import re

def check_links(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    for url in urls:
        try:
            r = requests.head(url, timeout=5)
            status = 'OK' if r.status_code == 200 else f'FAIL ({r.status_code})'
        except Exception as e:
            status = f'ERROR ({e})'
        print(f'Link: {url} -> {status}')

if __name__ == '__main__':
    check_links('portfolio.html')
