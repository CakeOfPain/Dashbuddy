from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/widgets", methods=["GET"])
def getWidgets():
    return {}, 200

@app.route("/api/widgets", methods=["POST"])
def postWidgets():
    return {}, 200