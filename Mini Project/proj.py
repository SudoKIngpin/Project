from flask import Flask,render_template,request
from pytube import YouTube 
# import requests 

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download',methods=["POST"])

def download():  
    url=request.form['url']
    yt=YouTube(url)
    y=str(yt)
    name="Harsh"

    return f'''Hello {y}'''


app.run(debug=True)