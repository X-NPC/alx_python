""" 
This following code should imporve on 1-hbnb_route.py file
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes= False)
def HellooHbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes= False)
def hbnb():
    return "HBNB"

#the added part
@app.route ('/c/<str:text>', strict_slashes= False)
def c_fun(text):
    #convert = str(text)
    txt= text.replace("_", " ")
    return ("C {}" .format(txt)) 

# I wonder if I could write all rooutes in one decorator insead of 3, but I have no time to come-up with the way to that

if __name__=="__main__":
    app.run(host= '0.0.0.0', port=5000)

#
