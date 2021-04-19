# exif


CREATE TABLE pictures_meta (
id INTEGER(22) auto_increment NOT NULL,
lens_model varchar(100),
focal_length_in3_5mm_film varchar(100),
focal_length varchar(100),
PRIMARY KEY(id)
)
