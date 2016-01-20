from flask import Flask, render_template, request
# from model import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("create.html")

@app.route('/form_submit', methods=['GET', 'POST'])
def form_submit():
    return test_function(request)

if __name__ == '__main__':
    app.run(debug = True)