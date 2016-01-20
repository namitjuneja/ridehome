from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/yes')
def yes_yes():
    return "okay"

if __name__ == '__main__':
    app.run(debug = True)