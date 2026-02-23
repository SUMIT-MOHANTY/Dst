from PIL import Image, ImageDraw, ImageFont

def create_test_image(path):
    img = Image.new('RGB', (800, 600), color='lightblue')
    draw = ImageDraw.Draw(img)
    draw.rectangle([100, 100, 700, 500], fill='white', outline='navy', width=3)
    draw.text((400, 300), 'Test Image', fill='black', anchor='mm')
    img.save(path)
    print(f'Created test image: {path}')

if __name__ == '__main__':
    os.makedirs('/workspace/images', exist_ok=True)
    create_test_image('/workspace/images/test.png')
