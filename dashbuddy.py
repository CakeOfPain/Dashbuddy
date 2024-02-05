# Flask App for Dashbuddy

import json

from flask import Flask, render_template, request
from pluginManager import PluginManager

app = Flask(__name__)

# Plugin Manager Config
pluginManager = PluginManager(app)
pluginManager.manage()

backgroundUrl = "https://images.unsplash.com/photo-1593291805141-990f40ec982d?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

@app.route("/")
def index():
    return render_template('index.html', imageUrl=backgroundUrl)

@app.route("/edit")
def editMode():
    return render_template('edit.html', imageUrl=backgroundUrl), 200

@app.get("/api/widgets")
def getWidgets():
    with open("./data/widgets.json", "r") as f:
        return json.load(f), 200

@app.post("/api/widgets")
def postWidgets():
    with open("./data/widgets.json", "w") as f:
        widgets = json.loads(request.data)
        json.dump(widgets, f)
        return {"message": "Widgets were saved"}, 201

@app.get("/api/plugins")
def listPlugins():
    return pluginManager.listPluginsJson(), 200

@app.get("/api/customization")
def get_methode():
    with open('./data/customization.json','r') as f:
        customization = json.load(f)
        return customization, 200

@app.post("/api/customization")
def post_methode():
    with open('./data/customization.json','w') as f:
        customization = json.loads(request.data)
        json.dump(customization,f)
        return {"message": "Customization successfully saved"}, 200

if __name__=='__main__':
    app.run(debug=True)