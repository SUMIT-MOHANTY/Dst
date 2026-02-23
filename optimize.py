#!/usr/bin/env python3
import os
from PIL import Image
import jsmin
import csscompressor

def optimize_image(input_path, output_path, quality=85):
    img = Image.open(input_path)
    img.save(output_path, 'WEBP', quality=quality, method=6)
    return True

def minify_css(input_path, output_path):
    with open(input_path, 'r') as f:
        content = f.read()
    minified = csscompressor.compress(content)
    with open(output_path, 'w') as f:
        f.write(minified)
    return minified

def minify_js(input_path, output_path):
    with open(input_path, 'r') as f:
        content = f.read()
    minified = jsmin.jsmin(content)
    with open(output_path, 'w') as f:
        f.write(minified)
    return minified

if __name__ == '__main__':
    optimize_image('test.png', 'test.webp')
    print('Optimization complete')
