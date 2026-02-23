import os
import re
from PIL import Image

def minify_css(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def minify_js(content):
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                img_path = os.path.join(input_dir, filename)
                img = Image.open(img_path).convert('RGB')
                out_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
                img.save(out_path, 'webp', quality=80)
                print(f'[IMAGE] {filename} -> WebP')
            except Exception as e:
                print(f'[ERROR] {filename}: {e}')

def process_code(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        in_path = os.path.join(input_dir, filename)
        out_path = os.path.join(output_dir, filename)
        with open(in_path, 'r') as f:
            content = f.read()
        if filename.endswith('.css'):
            with open(out_path, 'w') as f:
                f.write(minify_css(content))
            print(f'[CSS] Minified {filename}')
        elif filename.endswith('.js'):
            with open(out_path, 'w') as f:
                f.write(minify_js(content))
            print(f'[JS] Minified {filename}')

if __name__ == '__main__':
    print('Starting optimization...')
    process_images('assets/images', 'public/images')
    process_code('assets/css', 'public/css')
    process_code('assets/js', 'public/js')
    print('Optimization complete.')
