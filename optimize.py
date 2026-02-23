import os
import json
import shutil
from pathlib import Path

CONFIG_PATH = '/workspace/config.json'

def load_config():
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'input_dir': '/workspace/assets', 'output_dir': '/workspace/www'}
    except json.JSONDecodeError as e:
        print(f'JSON decode error: {e}')
        return {'input_dir': '/workspace/assets', 'output_dir': '/workspace/www'}

def minify_css(content):
    lines = content.split('\n')
    return ''.join(line.strip() for line in lines if line.strip() and not line.strip().startswith('/*'))

def minify_js(content):
    lines = content.split('\n')
    minified = ''.join(line.strip().rstrip(';') + ';' for line in lines if line.strip() and not line.strip().startswith('//'))
    return minified.rstrip(';')

def optimize():
    config = load_config()
    input_dir = Path(config.get('input_dir', '/workspace/assets'))
    output_dir = Path(config.get('output_dir', '/workspace/www'))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for css_file in input_dir.glob('**/*.css'):
        rel_path = css_file.relative_to(input_dir)
        out_file = output_dir / rel_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        with open(css_file, 'r') as f:
            minified = minify_css(f.read())
        with open(out_file, 'w') as f:
            f.write(minified)
    
    for js_file in input_dir.glob('**/*.js'):
        rel_path = js_file.relative_to(input_dir)
        out_file = output_dir / rel_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        with open(js_file, 'r') as f:
            minified = minify_js(f.read())
        with open(out_file, 'w') as f:
            f.write(minified)
    
    print('Optimization complete')

if __name__ == '__main__':
    optimize()
