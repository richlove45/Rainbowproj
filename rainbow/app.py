from flask import Flask, render_template, current_app as app
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Richlove's Rainbow Project"

#def = function. Create 7 routes for the rainbow colors using this template. 
@app.route('/red')
def red():
    return render_template() 

@app.route('/Orange')
def Orange():
    return render_template()

@app.route('/Yellow')
def Yellow():
    return render_template()

@app.route('/Green')
def Green():
    return render_template()

@app.route('/Blue')
def Blue():
    return render_template()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')