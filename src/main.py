from flask import Flask, send_file, request
import json
from api.main import api_bp
from db import connect

app = Flask(__name__, static_folder="static", static_url_path="/")
app.register_blueprint(api_bp)

CONFIG = json.load(open("config.json", "r"))

connect()

@app.route("/")
def home():
    return send_file("static/index.html")

@app.route("/test") # this is the url you visit in the browser: http://localhost:5000/test
def test(): # this is the function name, it doesnt matter what it is, but it MUST BE UNIQUE
    return send_file("static/test.html") # this is the path to the html file that is served
# add more pages here by copy pasting above...

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host="0.0.0.0"
    )
