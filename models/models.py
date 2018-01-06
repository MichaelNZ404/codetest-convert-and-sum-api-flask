import json

class Price():
    def __init__(self):
        self.data = {}
        price_info = json.load(open('pricing.json'))
        vat = price_info['vat_bands']

        for data in price_info['prices']:
            data['vat_rate'] = vat[data['vat_band']]
            data['vat_amount'] = data['price']*data['vat_rate']
            data['incl_vat'] = data['price']+data['vat_amount']
            self.data[data['product_id']] = data
