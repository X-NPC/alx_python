""" 
related to task 2
"""

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


@app.route ('/c/<string:text>', strict_slashes= False)
def c_fun(text):
    
    txt= text.replace("_", " ")
    return ("C {}" .format(txt)) 

#the added part
@app.route ('/python/<text="is cool">', strict_slashes= False)
def python_is_cool(text):
    txt= text.replace("_", " ")
    return "Python {}" .format(text)

if __name__=="__main__":
    app.run(host= '0.0.0.0', port=5000)

#
