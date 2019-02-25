import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flaskext.mysql import MySQL
from random import *

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
CORS(app)

mysql = MySQL()
mysql.init_app(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT',5000)),debug=True)