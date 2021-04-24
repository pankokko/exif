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
    # print(f"{tag_id}: {value}")
    tag = TAGS.get(tag_id, tag_id)
    # Sigma 30mm F1.4は分析する必要はない。
    if tag == 'FocalLength' and value[0] != 460 :
      focal_length = value[0] * 0.1
      print(f'実焦点距離：{focal_length}')
      cursor.execute("INSERT INTO pictures_meta (focal_length) values(%s)" , (focal_length,))
      connection.commit()
 
# 接続を閉じる
connection.close()