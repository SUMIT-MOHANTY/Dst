from PIL import Image
import os

def optimize_image(input_path, output_path, quality=80):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'WebP', quality=quality, method=6)
            print(f'Optimized: {input_path} -> {output_path}')
            return True
    except Exception as e:
        print(f'Error optimizing {input_path}: {e}')
        return False

def optimize_all_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, os.path.splitext(rel_path)[0] + '.webp')
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                optimize_image(input_path, output_path)

if __name__ == '__main__':
    optimize_all_images('assets/images', 'dist/images')
