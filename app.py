import os
import time
from flask import Flask, render_template, request, jsonify
from num2words import num2words
import decimal

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create-cheque', methods=['POST'])
def create_cheque():
    in_words = request.form['automation-amount']
    try:
        in_words = num2words(in_words).replace('-', ' ')
        #in_words = in_words.title()
    except (ValueError, decimal.InvalidOperation):
        return render_template('error.html')
    return render_template('cheque.html', result={'amount': request.form['automation-amount'], 'in_words': in_words})


@app.route('/list', methods=['GET'])
def list_cheques():
    cheques = [{
        'name': 'Mark',
        'amount': 200
    },
    {
        'name': 'John',
        'amount': 123.9
    }]
    return jsonify(cheques)


if __name__ == "__main__":
    time.sleep(5)
    app.run(host="0.0.0.0", port=5001, debug=False)
