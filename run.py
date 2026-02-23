import os
from image_optimizer import process_images
from minifier import minify_css, minify_js

if __name__ == '__main__':
    print('Starting optimization...')
    in_dir = 'assets/images'
    out_dir = 'assets/optimized'
    if os.path.exists(in_dir):
        process_images(in_dir, out_dir)
        print(f'Optimized images to {out_dir}')
    else:
        print(f'No images found in {in_dir}')
    print('Minification utilities ready.')
