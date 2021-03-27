from flask import Flask, request, redirect, url_for, render_template, current_app as app
from sense_hat import SenseHat

app = Flask(__name__)

sense = SenseHat()
sense.show_message()

@app.route('/')
def index():
    return "Welcome to Richlove's Login Page" 

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      return render_template("login.html")

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')
