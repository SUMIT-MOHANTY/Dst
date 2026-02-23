import re

def minify_css(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    content = content.replace(' {', '{').replace('{ ', '{')
    content = content.replace(' :', ':').replace(': ', ':')
    return content.strip()

def minify_js(content):
    content = re.sub(r'//.*?\n', '\n', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = content.replace('var ', 'var ').replace('let ', 'let ')
    return content.strip()
