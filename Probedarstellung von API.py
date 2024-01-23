# API-Entwicklung von Sebastian Beispiel

# Import von Hilfspaketen

from flask import Flask
from flask import request
import json

# GET-Method programmieren

app1=Flask(__name__)

@app1.route('/api/empty',methods=['GET'])
def leer_get():
    with open('get.json','w') as f:
        json.dump({},f)
        return"Leerer File GET",200

# POST-Methode programmieren

@app1.route('/api/empty',methods=['POST'])
def post_leer():
    with open('post.json','w') as f:
        json.dump({},f)
        return"Leerer File POST",200
    

if __name__=='__main__':
    app1.run(debug=True)
