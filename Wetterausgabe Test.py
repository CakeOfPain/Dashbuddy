# import das Wetter ausgeben (vom Deutschen Wetterdienst scrapen)

import requests
import webbrowser
from flask import Flask

# Funktion für Wetter scrapen

app=Flask(__name__)
@app.route("/wetter",methods=['GET'])

def wetterscraper():
    url=f"https://app-prod-ws.warnwetter.de/v30/stationOverviewExtended?stationIds=10865,G005"
    antwort = requests.get(url)
    if antwort.status_code==200:
        return antwort.json
    if antwort.status_code==404:
        return webbrowser.open('https://http.cat/status/404')
    if antwort.status_code==405:
        return webbrowser.open('https://http.cat/status/405')
    if antwort.status_code==418:
        return webbrowser.open('https://http.cat/status/418')
    else:
        return ('Unintendet Failure')
    
if __name__ == '__main__':
    app.run(debug=True)
