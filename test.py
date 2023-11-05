from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("test.html")

@app.route("/download",methods=["GET","POST"])
def poste():
    user=request.form
    return user
app.run(debug=True)