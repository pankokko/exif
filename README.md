<h2>rawファイルかjpegからmeta情報を取り出し分析するPythonアプリケーション</h2>

<h2>目的</h2>
<h4>自身のよく使う焦点距離やF値を分析し癖を知る、次に買うレンズを決める際の参考にできる<h4>

 <h2>使い方</h2>
  <p>jpgファイルにのみ使えるプログラムとなっている</p>
    <p>rawファイルを直接選択してクイックアクション　→ 「raw to jpeg」を選択後のファイルにのみ使うことができる</p>

 
 <h2> ■重要項目 </h2>
 
<p> Fnumber (14, 5) 配列型　[0]と[1]を割った値が実際のF値と思われる (14 ÷ 5 = 2.8)　</p>
<p>  FocalLength (18, 1)   配列型　[0]で実際のレンズの設定が表示されている。 35mm換算はされていない <p/>
<p>  FocalLengthIn35mmFilm int型　フルサイズ換算した時の焦点距離が記録されている。 </p>
 
<h2>テーブル作成</h2>

 
<h3>CREATE TABLE pictures_meta_new ( id INTEGER(22) auto_increment NOT NULL, lens_model varchar(100), focal_length_35mm_film varchar(100), focal_length varchar(100), f_number varchar(100), PRIMARY KEY(id) )
 </h3>
 
