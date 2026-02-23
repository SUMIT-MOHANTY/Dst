import re

def minify_js(js_content):
    js = re.sub(r'//.*', '', js_content)
    js = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    js = re.sub(r'\s+', ' ', js)
    js = re.sub(r'\s*([{}();,:+\-=<>!&|])\s*', r'\1', js)
    js = re.sub(r'\s*([\[\]])\s*', r'\1', js)
    js = js.strip()
    return js

def minify_js_file(input_path, output_path=None):
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.min.js"
    with open(input_path, 'r') as f:
        content = f.read()
    minified = minify_js(content)
    with open(output_path, 'w') as f:
        f.write(minified)
    print(f"Minified JS: {input_path} -> {output_path}")
    return output_path
