from flask import Flask

# python -m venv .venv
# py -3 -m venv .venv
# source .venv/Scripts/activate
# pip install Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello Galaxy!</p>"

# clone repo
# create branch
# make changes
# commit and push
