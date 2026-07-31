from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/about/<name>')
def hello_name(name):
    return f"Hello {name}"

@app.route('/contact')
def contact():
    
    return render_template("index.html")


if __name__ == '__main__': # __main__ = app.py
    app.run(port=8080, debug=True)