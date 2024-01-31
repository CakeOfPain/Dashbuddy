from flask import render_template
from bs4 import BeautifulSoup
import requests

def getWeather():
     url=f"https://www.google.com/search?q=wetter"
     antwort=requests.get(url)
     soup=BeautifulSoup(antwort.text,'html.parser')
     location = soup.find('div',attrs={'id':'wob_loc'}).text
     time = soup.find('div',attrs={'id':'wob_dts'}).text
     info = soup.find('div',attrs={'id':'wob_dc'}).text
     temp = soup.find('div',atters={'id':'wob_tm'}).text
     return(location,time,info,temp+'°C')


def getContent():
    return render_template("weather/index.html"),200


def createPlugin(plugin):
    plugin.name("weather")
    plugin.describe("prints put current weather")
    plugin.api("weather", getWeather)
    plugin.content(getContent)