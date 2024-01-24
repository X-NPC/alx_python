""" 
This code should start a flask webapp
"""
from flask import Flask

app = Flask(__name__)

if __name__=="__main__":
    app.run()