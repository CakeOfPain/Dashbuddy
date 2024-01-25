from flask import Flask, render_template, request
from pluginManager import PluginManager
import json

app = Flask(__name__)

pluginManager = PluginManager(app)
pluginManager.manage()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/widgets", methods=["GET"])
def getWidgets():
    with open("./data/widgets.json", "r") as f:
        return json.load(f), 200

@app.route("/api/widgets", methods=["POST"])
def postWidgets():
    with open("./data/widgets.json", "w") as f:    
        widgets = json.loads(request.data)
        json.dump(widgets, f)
        return {"message": "Widgets were saved"}, 201

@app.get("/api/plugins")
def listPlugins():
    return pluginManager.listPluginsJson(), 200
