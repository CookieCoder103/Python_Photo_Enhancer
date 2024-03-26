from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'

pathOut = './editedImgs'

if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))
    
img - img.convert('RGB')
    
edit = img.filter(ImageFilter.SMOOTH)
edit = img.filter(ImageFilter.BLUR)
    
img_con = ImageEnhance.Contrast(img)
img_con.enhance(1.3)
    
    
clean_name = os.path.splitext(filename)[0]
    
edit.save(os.path.join(pathOut, f'{clean_name}_edited.png'))