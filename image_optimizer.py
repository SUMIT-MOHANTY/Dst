import os
from PIL import Image

def optimize_image(input_path, output_path=None, quality=85):
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.webp"
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'WEBP', quality=quality, method=6)
        print(f"Optimized: {input_path} -> {output_path}")
        return output_path
    except Exception as e:
        print(f"Error optimizing {input_path}: {e}")
        return None

def optimize_directory(input_dir, output_dir=None):
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                if output_dir:
                    rel_path = os.path.relpath(input_path, input_dir)
                    output_path = os.path.join(output_dir, os.path.splitext(rel_path)[0] + '.webp')
                else:
                    output_path = None
                optimize_image(input_path, output_path)
