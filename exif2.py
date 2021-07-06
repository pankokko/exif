from PIL import Image
from PIL.ExifTags import TAGS
from PIL.MpoImagePlugin import MpoImageFile
import glob
import MySQLdb

connection = MySQLdb.connect(
  host='localhost',
  user='root',
  passwd='',
  db='python_db')

cursor = connection.cursor()

images = glob.glob("/Users/teshigawararyou/desktop/jpeg_pics/*.jpg")

for path in images : # path = 読み込みたい画像ファイルのパス

# 読み込み
  im: MpoImageFile = Image.open(path)

  exif = im.getexif()

  # tag_idはExif情報のキー、valueはExif情報の値。
  # tag_idはstr型ではないので、TAGS.getメソッドによってstr型に変換する
  for tag_id, value in exif.items():
    tag = TAGS.get(tag_id, tag_id)
    # print(f'{tag}: {value}')
    if tag == 'FocalLength' :   
      focal_length = value[0]
      cursor.execute("INSERT INTO pictures_meta_new (focal_length) values(%s)" , (focal_length,))
      connection.commit()
    if tag == 'FocalLengthIn35mmFilm':
      focal_length_35mm_film = value
      cursor.execute("INSERT INTO pictures_meta_new (focal_length_35mm_film) values(%s)" , (focal_length_35mm_film,))
      connection.commit()
    if tag == 'FNumber':
      f_number = value[0] / value[1]
      cursor.execute("INSERT INTO pictures_meta_new (f_number) values(%s)" , (f_number,))
      connection.commit()
    if tag == 'LensModel':
      lens_model = value
      cursor.execute("INSERT INTO pictures_meta_new (lens_model) values(%s)" , (lens_model,))
      connection.commit()

connection.close()