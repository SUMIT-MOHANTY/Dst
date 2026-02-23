#!/usr/bin/env python3
import os
import sys
from PIL import Image

def minify_css(content):
    lines = content.split('\n')
    result = []
    for line in lines:
        cleaned = line.strip()
        if cleaned and not cleaned.startswith('/*'):
            result.append(cleaned)
    return ' '.join(result).replace('  ', ' ')

def minify_js(content):
    return content.replace('\n', ' ').replace('  ', ' ').strip()

def optimize_to_webp(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')
        img.save(output_path, 'WEBP', quality=quality)
    print(f'Optimized: {input_path} -> {output_path}')

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            ext = file.lower().rsplit('.', 1)[-1]
            
            if ext in ('jpg', 'jpeg', 'png'):
                output_path = filepath.rsplit('.', 1)[0] + '.webp'
                try:
                    optimize_to_webp(filepath, output_path)
                except Exception as e:
                    print(f'Error optimizing {filepath}: {e}')
            
            elif ext == 'css':
                with open(filepath, 'r') as f:
                    content = f.read()
                minified = minify_css(content)
                with open(filepath, 'w') as f:
                    f.write(minified)
                print(f'Minified CSS: {filepath}')
            
            elif ext == 'js':
                with open(filepath, 'r') as f:
                    content = f.read()
                minified = minify_js(content)
                with open(filepath, 'w') as f:
                    f.write(minified)
                print(f'Minified JS: {filepath}')

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    process_directory(target_dir)
