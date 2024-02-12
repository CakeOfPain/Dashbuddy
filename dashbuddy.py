# Flask App for Dashbuddy

import json

from flask import Flask, render_template, request
from pluginManager import PluginManager

app = Flask(__name__)

# Plugin Manager Config
pluginManager = PluginManager(app)
pluginManager.manage()

backgrounds = [
    "https://images.unsplash.com/photo-1511898656451-9a7ad8dee728?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1664784805178-2c82a8e4b9c4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1522885147691-06d859633fb8?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1604065781162-602728f326a7?q=80&w=2533&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://content.presspage.com/uploads/1376/1920_leadimage-503702.jpg?10000",
    "https://images.unsplash.com/photo-1509356843151-3e7d96241e11?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1526644253653-a411eaafdfe6?q=80&w=2676&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
]

@app.route("/")
def index():
    return render_template('index.html', imageUrl=backgrounds[4], backgroundImage1=backgrounds[0], backgroundImage2=backgrounds[1], backgroundImage3=backgrounds[2], backgroundImage4=backgrounds[3], backgroundImage5=backgrounds[4], backgroundImage6=backgrounds[5], backgroundImage7=backgrounds[6], backgroundImage8=backgrounds[7])

@app.route("/edit")
def editMode():
    return render_template('edit.html', imageUrl=backgrounds[4], backgroundImage1=backgrounds[0], backgroundImage2=backgrounds[1], backgroundImage3=backgrounds[2], backgroundImage4=backgrounds[3], backgroundImage5=backgrounds[4], backgroundImage6=backgrounds[5], backgroundImage7=backgrounds[6], backgroundImage8=backgrounds[7]), 200

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