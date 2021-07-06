<h2>rawファイルかjpegからmeta情報を取り出し分析するPythonアプリケーション</h2>

<h2>目的</h2>
<h4>自身のよく使う焦点距離やF値を分析し癖を知る、次に買うレンズを決める際の参考にできる<h4>

 <h2>使い方</h2>
  <p>jpgファイルにのみ使えるプログラムとなっている</p>
    <p>rawファイルを直接選択してクイックアクション　→ 「raw to jpeg」を選択後のファイルにのみ使うことができる</p>

  
  
<h2>作成中</h2>


CREATE TABLE pictures_meta (
id INTEGER(22) auto_increment NOT NULL,
lens_model varchar(100),
focal_length_in3_5mm_film varchar(100),
focal_length varchar(100),
PRIMARY KEY(id)
)

  
 
