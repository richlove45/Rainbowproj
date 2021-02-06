from flask import Flask, render_template, current_app as app
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Richlove's Rainbow Project"

#def = function. Create 7 routes for the rainbow colors using this template. 
@app.route('/Red')
def Red():
    return render_template("red.html") 

@app.route('/Orange')
def Orange():
    return render_template("orange.html")

@app.route('/Yellow')
def Yellow():
    return render_template("yellow.html")

@app.route('/Green')
def Green():
    return render_template("green.html")

@app.route('/Blue')
def Blue():
    return render_template("blue.html")

@app.route('/Indigo')
def Indigo():
    return render_template("indigo.html")

@app.route('/Violet')
def Violet():
    return render_template("violet.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')