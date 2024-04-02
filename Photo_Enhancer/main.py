from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))
    
img = img.convert("RGB")

edit = img.filter(ImageFilter.SMOOTH_MORE)
edit = img.filter(ImageFilter.BLUR)

enhancer = ImageEnhance.Contrast(edit)
edited_img = enhancer.enhance(1.25)

clean_name = os.path.splitext(filename)[0]
edited_img.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))