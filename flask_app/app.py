from flask import Flask, render_template

app = Flask(__name__)


@app.route('/setup')
def setup():
    return render_template("setup_my_site.html")


@app.route('/css')
def css():
    return render_template("my_css.html")
