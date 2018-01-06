import pytest

from models.models import Price
from start import calculate_cart_totals

@pytest.fixture(scope="session")
def get_price():
    ''' load price once for all tests '''
    return Price()

def test_calculate_cart_totals():
    payload = {
      "currency": "GBP",
    	"order": {
    		"id": 12345,
    		"customer": {
    			...
    		},
    		"items": [
    			{
    				"product_id": 1,
    				"quantity": 1
    			},
    			{
    				"product_id": 2,
    				"quantity": 5
    			},
    			{
    				"product_id": 3,
    				"quantity": 1
    			}
    		]
    	}
    }
    response = calculate_cart_totals(payload)
    assert response['exchange_rate'] == 1
    assert response['total_price'] == 2099
    assert response['total_vat'] == 119.8

    assert response['items'][2]['price'] == 1250
    assert response['items'][2]['vat_amount'] == 0

def test_currency_lookup_changes rate():
    payload = {
      "currency": "NZD",
    	"order": {
    		"id": 12345,
    		"customer": {
    			...
    		},
    		"items": [
    			{
    				"product_id": 1,
    				"quantity": 1
    			},
    			{
    				"product_id": 2,
    				"quantity": 5
    			},
    			{
    				"product_id": 3,
    				"quantity": 1
    			}
    		]
    	}
    }
    response = calculate_cart_totals(payload)
    assert response['exchange_rate'] != 1
