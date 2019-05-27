from flask import Flask
app = Flask(__name__)

@app.route('/') # decorator function

def hello_world():
    return '<h1>Hello, WORLD!!!</h1>'

@app.route('/hello')

def hello():
    return "<h1>Daddy's Home!!!!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
