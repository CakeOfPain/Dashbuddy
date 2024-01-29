# Flask App for Dashbuddy

import json

from flask import Flask, render_template, request
from pluginManager import PluginManager
from unsplash.api import Api
from unsplash.auth import Auth

app = Flask(__name__)

# Plugin Manager Config
pluginManager = PluginManager(app)
pluginManager.manage()

# Unsplash API Config
client_id = "558839"
client_secret = ""
redirect_uri = ""
code = ""

lofotenBackground = "https://images.unsplash.com/photo-1593291805141-990f40ec982d?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
lapplandBackground = "https://images.unsplash.com/photo-1651363351227-a6ce6c761625?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
welcomeToHellBackground = "https://content.presspage.com/uploads/1376/1920_leadimage-503702.jpg?10000"

backgroundUrl = "https://images.unsplash.com/photo-1639471199129-94a07ab77b33?q=80&w=3167&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

#unsplashApiAuth = Auth(client_id, client_secret, redirect_uri, code=code)
#unsplash = Api(unsplashApiAuth)

@app.route("/")
def index():

    # Download new Image
    #imageId = unsplash.photo.random()
    #unsplashDownload = unsplash.photo.download(imageId)
    #unsplashDownload = "https://images.unsplash.com/photo-1650502446384-a07e09609ed7?ixid=M3w4ODczOHwwfDF8cmFuZG9tfHx8fHx8fHx8MTcwNjE4MDYwMnw&ixlib=rb-4.0.3&w=1512&h=982&dpr=2&auto=format&q=60&fit=crop"

    return render_template('index.html', imageUrl=welcomeToHellBackground)

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
