from flask import Flask, render_template, request
from pluginManager import PluginManager
import json

app = Flask(__name__)

pluginManager = PluginManager(app)
pluginManager.manage()

@app.route("/")
def index():
    return render_template('index.html')

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

@app.get("/get/empty")
def get_methode():
    with open('./data/customization.json','r') as f:
        customization = json.load(f)
        return customization, 200

@app.post("/post/empty")
def post_methode():
    with open('./data/customization.json','w') as f:
        customization = json.loads(request.data)
        json.dump(customization,f)
        return {"message": "Customization successfully saved"}, 200

if __name__=='__main__':
    app.run(debug=True)