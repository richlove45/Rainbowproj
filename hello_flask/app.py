from flask import Flask,render_template
#import datetime import date
import requests

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    name = 'Richlove Nkansah'
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p> My name is Richlove</p>'

@app.route('/nasa')
#def show_nasa_nasa will be ran when teh app.route endpoint is ran. Its a function.
    def show_nasa_pic()
        today = str(date.today())
        response.requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
        data = response.json()
        return render_template('nasa.html', data = data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


