from flask import Flask
from flask import render_template
import time as t
# import jsonify
import json

app = Flask(__name__)


@app.route('/home')
def home(): 
    with open('house_statisic.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
