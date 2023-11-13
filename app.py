from flask import Flask, render_template, request, flash
from utils import is_valid_currency, convert_currency

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Constants
EXCHANGE_API_URL = "https://api.exchangerate.host/convert"
VALID_CODES = {'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'}  # Add more valid codes as needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency').upper()
        to_currency = request.form.get('to_currency').upper()
        amount = request.form.get('amount')

        if not is_valid_currency(from_currency, VALID_CODES) or not is_valid_currency(to_currency, VALID_CODES):
            flash("Invalid currency code.")
            return render_template('form.html')

        try:
            amount = float(amount)
        except ValueError:
            flash("Invalid amount.")
            return render_template('form.html')

        data = convert_currency(from_currency, to_currency, amount, EXCHANGE_API_URL)
        if data and 'result' in data:
            result = round(data['result'], 2)
            return render_template('result.html', from_currency=from_currency, to_currency=to_currency, amount=amount, result=result)
        else:
            flash("Error with currency conversion.")
            return render_template('form.html')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
