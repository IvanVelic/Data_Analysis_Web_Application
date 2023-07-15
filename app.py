from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', active='home')

@app.route('/all')
def all_ads():
    return render_template('all.html', active='all')

@app.route('/audi')
def audi():
    return render_template('audi.html', active='audi')

@app.route('/ford')
def ford():
    return render_template('ford.html', active='ford')

@app.route('/mercedes')
def mercedes():
    return render_template('mercedes.html', active='mercedes')

@app.route('/opel')
def opel():
    return render_template('opel.html', active='opel')

@app.route('/renault')
def renault():
    return render_template('renault.html', active='renault')

@app.route('/seat')
def seat():
    return render_template('seat.html', active='seat')

@app.route('/skoda')
def skoda():
    return render_template('skoda.html', active='skoda')

@app.route('/volkswagen')
def volkswagen():
    return render_template('volkswagen.html', active='volkswagen')

@app.route('/back')
def go_back():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
