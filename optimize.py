import os
import sys
from image_optimizer import optimize_directory, optimize_image
from css_minifier import minify_css_file
from js_minifier import minify_js_file

def main():
    print("Starting web optimization...")
    
    # Create directories
    os.makedirs('input/images', exist_ok=True)
    os.makedirs('input/css', exist_ok=True)
    os.makedirs('input/js', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # Optimize images
    print("Optimizing images...")
    optimize_directory('input/images', 'output/images')
    
    # Optimize CSS
    print("Minifying CSS...")
    for file in os.listdir('input/css'):
        if file.endswith('.css'):
            minify_css_file(f'input/css/{file}', f'output/{file.replace(".css", ".min.css")}')
    
   # Optimize JS
    print("Minifying JS...")
    for file in os.listdir('input/js'):
        if file.endswith('.js'):
            minify_js_file(f'input/js/{file}', f'output/{file.replace(".js", ".min.js")}')
    
    print("Optimization complete!")

if __name__ == '__main__':
    main()
