import sqlite3
from flask import Flask, abort, render_template, url_for, request, redirect, g
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///" +os.getcwd()+ "/dbase/immanuwel.db")
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

@app.route("/")
def home():    
    return render_template("home.html")

@app.route("/index")
def index():    
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/album")
def album():
    audio = db.execute("SELECT album_name, author_name, album_ref, img_path FROM audio_album GROUP BY album_ref").fetchall()
    return render_template("album.html", audio=audio)


@app.route("/album_view")
def album_view():
    ref = ['IMM-01', 'DTP-02']
    err = False
    m = request.args.get('m') #Get the value of the parameter m in the URL query
    
    for q in ref:
        if m not in ref:
            err = True
            return redirect('album')
        if m is None or m =='' or m == True: 
            return redirect('album')

       
       #SQLAlchemy request
    try:        
        r = db.execute("SELECT * FROM audio_album WHERE album_ref=:album_ref", {"album_ref" : m}).fetchall()
        s = db.execute("SELECT * FROM audio_album GROUP BY album_ref").fetchall()
        v = db.execute("SELECT * FROM audio_album WHERE album_ref=:album_ref GROUP BY album_ref", {"album_ref" : m}).fetchall()                
        return render_template("album_view.html", r = r, s=s, v=v, m=m, err=err)

    except TypeError:
        print ('Demande non trouvee !')
        return redirect('album')

@app.route("/music")
def music():
    return render_template("podcast.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/single_blog")
def single_blog():
    return render_template("single_blog.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/worshiplive")
def worshiplive():
    rq = db.execute("SELECT * FROM video_worship GROUP BY video_ref").fetchall()
    return render_template("worshiplive.html", rq=rq)

@app.route("/exhortation")
def exhortation():
    exh = db.execute("SELECT * FROM video_exhortation GROUP BY video_ref").fetchall()
    return render_template("exhortation.html", exh=exh)

@app.route("/solo")
def solo():
    return render_template("solo.html")

@app.route("/recueil")
def recueil():
    return render_template("recueil.html")

@app.route("/podcast")
def podcast():
    return render_template("podcast.html")

@app.route("/lyrics")
def lyrics():
    r1 = db.execute("SELECT * FROM video_lyrics GROUP BY video_ref").fetchall()
    return render_template("lyrics.html", r1=r1)

@app.route("/lyrics_view")
def lyrics_view():
    ref = ['LYCS-01', 'LYCS-02', 'LYCS-03', 'LYCS-04', 'LYCS-05', 'LYCS-06']    
    v = request.args.get('v') #Get the value of the parameter v in the URL query
    
    for q in ref:
        if v not in ref:
            return redirect('lyrics')
        if v is None or v =='' or v == True: 
            return redirect('lyrics')

       
       #SQLAlchemy request
    try:
        #Request for viewing video
        r1 = db.execute("SELECT * FROM video_lyrics WHERE video_ref=:video_ref", {"video_ref" : v}).fetchall()
        #Request for viewing other videos
        r2 = db.execute("SELECT * FROM video_lyrics GROUP BY video_ref").fetchall()
        return render_template("lyrics_view.html", r1=r1, v=v, r2=r2)
    except TypeError:
        print ('Demande non trouvee !')
        return redirect('lyrics')

@app.route("/exhortation_view")
def exhortation_view():
    ref = ['EXHT-01', 'EXHT-02', 'EXHT-03',  'EXHT-04', 'EXHT-05', 'EXHT-06']
    v = request.args.get('v') #Get the value of the parameter v in the URL query
    
    for q in ref:
        if v not in ref:
            return redirect('exhortation')
        if v is None or v == '' or v == True:
            redirect('exhortation')

    #Database connection attempt

    try:
        r1 = db.execute("SELECT * FROM video_exhortation WHERE video_ref=:video_ref", {'video_ref' : v}).fetchall()
        r2 = db.execute("SELECT * FROM video_exhortation GROUP BY video_ref").fetchall()
        return render_template('exhortation_view.html', r1=r1, r2=r2, v=v)
    except TypeError:
        print('Demande non trouvée !')
        return redirect('exhortation')

@app.route("/worshiplive_view")
def worshiplive_view():
    ref = ['WSHP-01', 'WSHP-02', 'WSHP-03', 'WSHP-04', 'WSHP-05', 'WSHP-06', 'WSHP-07', 'WSHP-08']    
    v = request.args.get('v') #Get the value of the parameter v in the URL query
    
    for q in ref:
        if v not in ref:            
            return redirect('worshiplive')
        if v is None or v =='' or v == True: 
            return redirect('worshiplive')

       #SQLAlchemy request
    try:
        r1 = db.execute("SELECT * FROM video_worship WHERE video_ref=:video_ref", {"video_ref" : v}).fetchall()
        r2 = db.execute("SELECT * FROM video_worship GROUP BY video_ref").fetchall()
        return render_template("worshiplive_view.html", r1=r1, v=v, r2=r2)

    except TypeError:
        print ('Demande non trouvee !')
        return redirect('lyrics')
    return render_template("exhortation_view.html")
    return render_template("worshiplive_view.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
