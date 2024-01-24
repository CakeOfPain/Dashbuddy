from flask import Flask, render_template
import plugins.framework as Widget

app = Flask(__name__)

@app.route("/")
def index():
    Widget.load()
    return render_template('index.html')