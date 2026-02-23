import jsmin
import os

def minify_js(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.js'):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, file)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(input_path, 'r') as f:
                    content = f.read()
                minified = jsmin.jsmin(content)
                with open(output_path, 'w') as f:
                    f.write(minified)
                print(f'Minified: {input_path} -> {output_path}')

if __name__ == '__main__':
    minify_js('assets/js', 'dist/js')
