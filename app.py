import os
from flask import Flask, render_template, request
from num2words import num2words
import decimal

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create-cheque', methods=['POST'])
def create_cheque():
    in_words = request.form['amount']
    try:
        in_words = num2words(in_words).replace('-', ' ')
        #in_words = in_words.title()
    except (ValueError, decimal.InvalidOperation):
        return render_template('error.html')
    return render_template('cheque.html', result={'amount': request.form['amount'], 'in_words': in_words})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
