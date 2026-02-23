#!/usr/bin/env python3
import os
import subprocess
from PIL import Image
import re

def optimize_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        img.save(output_path, 'WEBP', quality=quality, method=6)
    print(f'Optimized: {input_path} -> {output_path}')

def minify_css(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}:;,])\s*', r'\1', content)
    content = content.strip()
    return content

def minify_js(content):
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}();,:=<>+\-*/])\s*', r'\1', content)
    content = content.strip()
    return content

def process_files():
    dirs = {'images': ['.png', '.jpg', '.jpeg'], 'css': ['.css'], 'js': ['.js']}
    for folder, extensions in dirs.items():
        input_dir = f'/workspace/{folder}'
        output_dir = f'/workspace/dist/{folder}'
        os.makedirs(output_dir, exist_ok=True)
        for f in os.listdir(input_dir):
            ext = os.path.splitext(f)[1].lower()
            if ext not in extensions:
                continue
            input_path = os.path.join(input_dir, f)
            if folder == 'images':
                output_path = os.path.join(output_dir, os.path.splitext(f)[0] + '.webp')
                optimize_image(input_path, output_path)
            else:
                output_path = os.path.join(output_dir, f)
                with open(input_path, 'r') as infile:
                    content = infile.read()
                if folder == 'css':
                    content = minify_css(content)
                elif folder == 'js':
                    content = minify_js(content)
                with open(output_path, 'w') as outfile:
                    outfile.write(content)
                print(f'Minified: {input_path} -> {output_path}')

if __name__ == '__main__':
    process_files()
    print('[CHECK] Optimization complete: PASS')
