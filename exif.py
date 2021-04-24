from PIL import Image
from PIL.ExifTags import TAGS
from PIL.MpoImagePlugin import MpoImageFile
import glob
import MySQLdb
from datetime import datetime as dt

connection = MySQLdb.connect(
  host='localhost',
  user='root',
  passwd='',
  db='python_db')

cursor = connection.cursor()

images = glob.glob("/Users/teshigawararyou/desktop/jpeg_pics/*.jpg")

for path in images : 

  im: MpoImageFile = Image.open(path)


  exif = im.getexif()
  
  dict = {"LensModel": "unknown", "Model": "unknown", "FocalLengthIn35mmFilm": "unknown", "FocalLength": "unknown", "DateTime": "1000-01-01 00:00:00.000000"}
  for tag_id, value in exif.items():
    tag = TAGS.get(tag_id, tag_id)

    if tag == 'LensModel':    
      dict["LensModel"] =  value
    if tag == 'Model':    
      dict["Model"] =  value
    if tag == 'FocalLengthIn35mmFilm':    
      dict["FocalLengthIn35mmFilm"] =  value
    if tag == 'FocalLength':
      dict["FocalLength"] =   value[0] * 0.1
    if tag == 'DateTime':
      dict["DateTime"] =  dt.strptime(value, '%Y:%m:%d %H:%M:%S')

    cursor.execute("INSERT INTO pictures_meta (lens_model, focal_length_in3_5mm_film, focal_length, date_time) values(%s, %s, %s, %s)" , (dict["LensModel"], dict["FocalLengthIn35mmFilm"], dict["FocalLength"], dict["DateTime"]))
    connection.commit()
connection.close()