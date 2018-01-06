import requests
import json

from flask import Flask, request, jsonify

from models.models import Price

app = Flask(__name__)
price = Price()

@app.route('/', methods = ['POST'])
def index():
    payload = request.get_json()
    response = calculate_cart_totals(payload)
    return jsonify(response)

def calculate_cart_totals(payload):
    if 'currency' in payload:
        rate = get_rate(payload['currency'])
    else:
        rate = 1

    response = {
        'items': {},
        'total_price': 0,
        'total_vat': 0,
        'exchange_rate': rate,
    }

    for item in payload['order']['items']:
        iid = item['product_id']
        item_price = round(price.data[iid]['price'] * item['quantity'] * rate, 2)
        item_vat = round(price.data[iid]['vat_amount'] * item['quantity'] * rate, 2)
        response['total_price'] += item_price
        response['total_vat'] += item_vat
        response['items'][iid] = {}
        response['items'][iid]['price'] = item_price
        response['items'][iid]['vat_amount'] = item_vat
    return response

def get_rate(currency_code):
    curr_url = 'https://api.fixer.io/latest?base=GBP'
    curr_response = requests.get(curr_url)
    if(curr_response.ok):
        return json.loads(curr_response.content)['rates'].get(currency_code, 1)
    else:
        curr_response.raise_for_status()
