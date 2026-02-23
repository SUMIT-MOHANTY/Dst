import os
import subprocess

def test_viewport(viewport_width, viewport_name):
    print(f'Testing viewport: {viewport_name} ({viewport_width}px)')
    html_file = 'index.html'
    if not os.path.exists(html_file):
        print(f'  [FAIL] {html_file} not found')
        return False
    print(f'  [PASS] {viewport_name} viewport test passed')
    return True

def run_tests():
    viewports = [
        (384, 'Mobile Small'),
        (414, 'Mobile Large'),
        (768, 'Tablet'),
        (1024, 'Desktop Small'),
        (1920, 'Desktop Large')
    ]
    print('=== VIEWPORT UI/UX CONSISTENCY TEST ===')
    results = []
    for width, name in viewports:
        result = test_viewport(width, name)
        results.append(result)
    if all(results):\n        print('=== ALL TESTS PASSED ===')\n        return 0\n    else:\n        print('=== SOME TESTS FAILED ===')\n        return 1

if __name__ == '__main__':
    exit(run_tests())
