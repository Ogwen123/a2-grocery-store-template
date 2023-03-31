from flask import Flask, send_file, request
import json

app = Flask(__name__)

#serve static html
@app.route("/")
def add():
    return send_file("../static/pages/index.html")

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host="0.0.0.0"
    )
