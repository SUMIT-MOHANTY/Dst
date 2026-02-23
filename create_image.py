from PIL import Image
img = Image.new('RGB', (800, 600), color='blue')
img.save('/workspace/image.png')
print('Image created')
