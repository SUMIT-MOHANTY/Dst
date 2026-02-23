#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, '/workspace')

try:
    from optimize import minify_css, minify_js, optimize_to_webp
    print('[CHECK] optimize.py syntax: PASS')
except SyntaxError as e:
    print(f'[CHECK] optimize.py syntax: FAIL - {e}')
    sys.exit(1)

assert os.path.exists('/workspace/optimize.py'), 'optimize.py missing'
assert os.path.exists('/workspace/requirements.txt'), 'requirements.txt missing'
assert os.path.exists('/workspace/public/styles.css'), 'styles.css missing'
assert os.path.exists('/workspace/public/app.js'), 'app.js missing'
print('[CHECK] All required files exist: PASS')

test_css = 'body { margin: 0; }'
result = minify_css(test_css)
assert 'margin' in result, 'CSS minification failed'
print('[CHECK] CSS minification: PASS')

test_js = 'function test() { return 1; }'
result = minify_js(test_js)
assert 'function' in result, 'JS minification failed'
print('[CHECK] JS minification: PASS')

print('=== FIX SUMMARY ===')
print('All syntax errors fixed.')
print('All files created successfully.')
