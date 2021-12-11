CREATE TABLE video_worship(
video_ref varchar(255),
video_title varchar(255),
video_author varchar(255),
video_subtitle varchar(255),
video_path text(2000),
pub_date date,
page_num integer);

INSERT INTO video_worship(video_ref, video_title, video_author, video_subtitle, video_path, pub_date, page_num, video_img) 
VALUES(
    'WSHP-01', 
    'J'irai là haut', 
    'Louis Raycla',
    '',
    'https://www.dailymotion.com/video/x7w2q4s',
    '10-09-2020',
    1,
    'static/img/bg-img/video-bg/video_caption_1_1.png');