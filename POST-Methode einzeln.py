from flask import Flask
from flask import request,jsonify
import json

app = Flask(__name__)

@app.route("/post/empty",methods=['POST'])
def post_methode():
    dateiname="post.json"
    data=request.get_json()
    if not data:
        data={}
    with open(dateiname,'w') as p:
        json.dump(data,p)
    return p

if __name__=='__main__':
    app.run(debug=True)