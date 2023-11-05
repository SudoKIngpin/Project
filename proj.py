from flask import Flask,render_template,request
from pytube import YouTube 
# import requests 

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download',methods=["GET","POST"])

def download():   
    url=request.form['url']
    yt=YouTube(url)
    title=yt.title
    video = yt.streams.first()
    video.download()

app.run(debug=True)