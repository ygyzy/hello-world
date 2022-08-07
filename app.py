from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><a href="https://ygyzy.github.io" >https://freetvbox.ml</a> </h1>"

@app.route('/<name>/')
def name(name):
    return "<h1> Hello, <span style='color:red;'>{} </span> ! </h2>".format(name)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0') 
