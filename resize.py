import os 
from PIL import Image

dirName = "/Users/teshigawararyou/desktop/before_resize"

newDirName = "/Users/teshigawararyou/desktop/resized"

files = os.listdir(dirName)
print(files)
for file in files:
  photo = Image.open(os.path.join(dirName, file))
  resizedPhoto = photo.resize((300,300))
  resizedPhoto.save(os.path.join(newDirName, file))