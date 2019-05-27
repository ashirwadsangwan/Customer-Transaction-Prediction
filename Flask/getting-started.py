from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>') # decorator function

def hello_world(name):
    return 'Hello, '+ str(name)

if __name__ == '__main__':
    app.run(debug=True)
