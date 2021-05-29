from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/op1')
def index():
    username = [ 'ANUBHAV','ALOK','SHLOK', ]
    return render_template('op1.html' , title = 'Welcome' , username = 'ALOK')

app.run(host='0.0.0.0', port=9000)
