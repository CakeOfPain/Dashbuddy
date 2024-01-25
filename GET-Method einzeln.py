# GET-Methode einzeln, wegen fehlerhafter Erstellung von Datei

from flask import Flask
import json
import requests

app = Flask(__name__)

url="https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"

@app.route("/get/empty",methods=['GET'])
def get_methode():
    response=requests.get(url)
    jason=response.json()
    with open('get.json','w') as g:
        g.write(json.dumps(jason)) 
    return g 

if __name__=='__main__':
    app.run(debug=True)