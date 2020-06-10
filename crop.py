# Improting Image class from PIL module
from PIL import Image
import os
from progress.bar import Bar
  
left = 0
top = 350
right = 2224
bottom = 1100

list = os.listdir("/Users/bokaili/Desktop/PianoSheetCrop/charlies")
bar = Bar('Processing', max=len(list))
for file in list:
        path=os.path.join("/Users/bokaili/Desktop/PianoSheetCrop/charlies", file)
        newPath=os.path.join("/Users/bokaili/Desktop/PianoSheetCrop/charliesNEW", file)
        im = Image.open(path)
        im1 = im.crop((left, top, right, bottom))
        im1.save(newPath)
        bar.next()
bar.finish()
print("Done")
