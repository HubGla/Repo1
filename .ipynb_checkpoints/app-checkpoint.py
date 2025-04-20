import sys
import subprocess

for package in ["Flask", "requests"]:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from flask import Flask, jsonify, request  # dodano 'request'

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Witaj w moim API'})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({'message': 'To jest moja strona'})

@app.route('/hello')
def hello():
    name = request.args.get('name', 'stranger')
    return jsonify({'Hello': name})  

@app.route('/predict')
def predict():
    x = float(request.args.get('num1', 0))
    y = float(request.args.get('num2', 0))
    z = x+y
    if z>5.8:
        return jsonify({'predict': 1}) 
    else:
        return jsonify({'predict': 0})
    

if __name__ == '__main__':
    app.run()
