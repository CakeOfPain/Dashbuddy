from flask import request, render_template

def createContent():
    noteText = request.args.get("text")
    return render_template("note/index.html", noteText=noteText), 200

def createPlugin(plugin):
    plugin.name("note")
    plugin.describe("Can be used for notes")
    plugin.content(createContent)