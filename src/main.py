from flask import Flask, send_file, request
import json
from api.main import api_bp

app = Flask(__name__, static_folder="static", static_url_path="/")
app.register_blueprint(api_bp)

#TODO mysql and config

@app.route("/")
def home():
    return send_file("static/index.html")

@app.route("/test")
def test():
    return send_file("static/test.html")
# add more pages here...

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host="0.0.0.0"
    )
