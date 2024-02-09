from flask import render_template
import requests

def getGifGiphy():
    def search_giphy(api_sch,suche):
        basisurl="https://api.giphy.com/v1/gifs/search"
        parameter={"api_key":api_sch, "q":suche, "limit":5}
        gif=requests.get(basisurl,parameter=parameter)
        if gif.status_code==200:
            return gif.json()
        else:
            return("Ein Fehler ist aufgetreten! \n\n Überprüfen Sie Ihre Internetverbindung. \n Überprüfen Sie die Browserkompabilität. \n Wenden Sie sich an einen Consultant.")
    
    ausgabe=search_giphy("FNA2D2tAS7ECtXZSUMqAh8z7PS8TfXdY","computerscience")
    if ausgabe:
        for git in ausgabe['Data']:
            return(git['url'])
    else:
        return("Anfrage war nicht erfolgreich!")

def getContent():
    return render_template("gif/index.html"), 200

def createPlugin(plugin):
    plugin.name("gif")
    plugin.describe("random gif")
    plugin.api("gif", getGifGiphy)
    plugin.content(getContent)