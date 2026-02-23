import os
from optimize_images import optimize_all_images
from minify_css import minify_css
from minify_js import minify_js

def build():
    print('Starting build process...')
    print('Optimizing images...')
    optimize_all_images('assets/images', 'dist/images')
    print('Minifying CSS...')
    minify_css('assets/css', 'dist/css')
    print('Minifying JS...')
    minify_js('assets/js', 'dist/js')
    print('Build complete!')

if __name__ == '__main__':
    build()
