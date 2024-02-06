# Imports von Hilfspaketen
# Flask ist ein in Python geschriebenes Mikro-WebFramework 
# Bei Flask wird ein minimalistischer Ansatz verwendet, es geht darum, dass der Kern möglichst einfach gehalten wird
from flask import render_template
import json
import requests

def getContent():
    return render_template("gif/index.html"), 200

# Diese Funktion erfragt über das requests-Hilfspaket eine Antwort von der Website, diese Website antwortet mit einem zufälligen GIF
def getGif():
    the_url="https://api.giphy.com/v1/gifs/trending/api_key=FNA2D2tAS7ECtXZSUMqAh8z7PS8TfXdY"
    response=requests.get(the_url)
    gif_data=response.json()
    gif_url=gif_data["data","image_url"]
    return gif_url

def createPlugin(plugin):
    plugin.name("gif")
    plugin.describe("random gif")
    plugin.api("gif", getGif)
    plugin.content(getContent)