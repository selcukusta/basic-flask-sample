from flask import Flask
from helpers import string_helper
app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h1>{0}</h1>".format(string_helper.trim_and_uppercase("    Hello World     "))