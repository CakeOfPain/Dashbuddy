from flask import Flask, render_template
from pluginManager import PluginManager

app = Flask(__name__)

pluginManager = PluginManager(app)
pluginManager.manage()

@app.route("/")
def index():
    return render_template('index.html')

@app.get("/api/plugins")
def listPlugins():
    return pluginManager.listPluginsJson(), 200