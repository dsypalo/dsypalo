from flask import Flask, render_template, request, redirect, url_for
#from application import db
#from application.models import Data


app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'cC1YCIWOj9GgWspgNEo2'

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')
@app.route('/index.html',methods=['POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
