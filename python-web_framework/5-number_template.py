""" 
related to task 4
"""

from flask import Flask, render_template

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


@app.route ('/python/<string:text>', strict_slashes= False)
def python(text='is_cool'):

    txt= text.replace("_", " ")
    return "Python {}" .format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    the_number = n
    return "{} is a number" .format(the_number)

#the add part below
@app.route('/number_template/<int:n>', strict_slashes= False)
def task_5(n):
    return render_template("5-number_template.html", n=int(n))


if __name__=="__main__":
    app.run(host= '0.0.0.0', port=5000)

#
