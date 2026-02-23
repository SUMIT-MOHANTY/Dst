#!/usr/bin/env python3
import os
import re

wf = lambda p,c: (os.makedirs(os.path.dirname(p),exist_ok=True),open(p,'w').write(c))

def minify_css(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}:;,])\s*', r'\1', content)
    return content.strip()

def minify_js(content):
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}();,=+:\[\]])\s*', r'\1', content)
    return content.strip()

def optimize_webp(input_path, output_path, quality=85):
    try:
        from PIL import Image
        img = Image.open(input_path)
        img.save(output_path, 'WEBP', quality=quality, optimize=True)
        return True
    except ImportError:
        print('PIL not installed')
        return False
    except Exception as e:
        print(f'Error: {e}')
        return False

def process_files():
    print('Starting optimization...')
    assets = {'styles.css': 'css', 'script.js': 'js'}
    for f, t in assets.items():
        if os.path.exists(f'/workspace/{f}'):
            with open(f'/workspace/{f}', 'r') as file:
                content = file.read()
            minified = minify_css(content) if t == 'css' else minify_js(content)
            wf(f'/workspace/dist/{f}.min', minified)
            print(f'Minified {f}')
    images = [f for f in os.listdir('/workspace') if f.lower().endswith(('.png','.jpg'))]
    for img in images:
        name = os.path.splitext(img)[0]
        if optimize_webp(f'/workspace/{img}', f'/workspace/dist/{name}.webp'):
            print(f'Converted {img} to WebP')
    print('Optimization complete!')

if __name__ == '__main__':
    os.makedirs('/workspace/dist', exist_ok=True)
    process_files()
