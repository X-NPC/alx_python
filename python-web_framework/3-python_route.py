""" 
related to task 2
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
@app.route ('/python/<text>', strict_slashes= False)
def python_is_cool(text="is_cool"):
    tempo_var = text
    txt= tempo_var.replace("_", " ")
    return ("Python {}" .format(txt))

if __name__=="__main__":
    app.run(host= '0.0.0.0', port=5000)

#
