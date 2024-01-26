from PIL import Image, ImageEnhance, ImageFilter
import os

# Use an absolute path
path = r'eduSite\Folder\pythonFolder\Image\imgs'
pathOut = r'eduSite\Folder\pythonFolder\Image\editedImgs'

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))

    # Example 1: Apply a sharpening filter
    edit = img.filter(ImageFilter.SHARPEN)

    # Example 2: Convert the image to grayscale
    edit = img.convert('L')

    # Example 3: Rotate the image counterclockwise by 90 degrees
    edit = img.rotate(-90)

    # Example 4: Enhance contrast by a factor of 1.5
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Save Edited Image
    clean_name = os.path.splitext(filename)[0]
    edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))

