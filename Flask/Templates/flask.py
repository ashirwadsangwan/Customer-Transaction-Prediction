from flask import render_template, Flask

app = Flask(__name__)

@app.route('/') # decorator function

def home():
    return render_template('home.html')

@app.route('/about')

def about():
    return "<h1>Daddy's Home!!!!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
