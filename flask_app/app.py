from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/setup')
def setup():
    return render_template("setup_my_site.html")


@app.route('/css')
def css():
    return render_template("my_css.html")
