from PIL import Image
import os

def create_test_image():
    os.makedirs('assets/images', exist_ok=True)
    img = Image.new('RGB', (800, 600), color='blue')
    img.save('assets/images/test.jpg', 'JPEG', quality=95)
    print('Created test image: assets/images/test.jpg')

if __name__ == '__main__':
    create_test_image()
