import os
from PIL import Image

def optimize_image(input_path, output_path, quality=80):
    try:
        img = Image.open(input_path)
        img.save(output_path, 'WebP', quality=quality, method=6)
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False

def process_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for f in os.listdir(input_dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = os.path.splitext(f)[0]
            optimize_image(os.path.join(input_dir, f), os.path.join(output_dir, name + '.webp'))
