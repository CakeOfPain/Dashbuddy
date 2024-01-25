from datetime import datetime
from flask import render_template

def getTime():
    return f"{datetime.now().strftime('%H:%M:%S')}", 200

def getContent():
    return render_template("watch/index.html"), 200

def createPlugin(plugin):
    plugin.name("watch")
    plugin.describe("Simple watch widget")
    plugin.api("time", getTime)
    plugin.content(getContent)