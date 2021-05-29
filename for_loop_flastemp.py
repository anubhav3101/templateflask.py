from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/op')
def index():
    users = [ 'ANUBHAV','ALOK','SHLOK' ]
    return render_template('op.html', title='Welcome', members=users)

app.run(host='0.0.0.0', port=9000)
