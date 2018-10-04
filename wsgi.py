import requests
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Welcome to World of python!"

if __name__ == "__main__":
    application.run()
