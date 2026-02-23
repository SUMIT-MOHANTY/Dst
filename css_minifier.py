import re

def minify_css(css_content):
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{}:;,])\s*', r'\1', css)
    css = css.strip()
    return css

def minify_css_file(input_path, output_path=None):
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.min.css"
    with open(input_path, 'r') as f:
        content = f.read()
    minified = minify_css(content)
    with open(output_path, 'w') as f:
        f.write(minified)
    print(f"Minified CSS: {input_path} -> {output_path}")
    return output_path
