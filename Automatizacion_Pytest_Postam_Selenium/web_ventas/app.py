from flask import Flask,render_template

#todo crear una web usando python-flask
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__=='__main__':
    app.run()
