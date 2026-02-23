import os
from PIL import Image
import re

def minify_css(content):
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def minify_js(content):
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def optimize_image(input_path, output_dir):
    if not os.path.exists(input_path):
        return
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}.webp")
    try:
        with Image.open(input_path) as img:
            img.save(output_path, "WEBP", quality=80, method=6)
            print(f"Optimized: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_files(src_dir, dist_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, src_dir)
            out_path = os.path.join(dist_dir, rel_path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            
            if file.endswith(('.png', '.jpg', '.jpeg')):
                optimize_image(full_path, os.path.dirname(out_path))
            elif file.endswith('.css'):
                with open(full_path, 'r') as f:
                    content = f.read()
                with open(out_path, 'w') as f:
                    f.write(minify_css(content))
            elif file.endswith('.js'):
                with open(full_path, 'r') as f:
                    content = f.read()
                with open(out_path, 'w') as f:
                    f.write(minify_js(content))
            else:
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                os.system(f"cp {full_path} {out_path}")

if __name__ == "__main__":
    process_files("./assets", "./public")
