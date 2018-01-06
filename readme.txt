Specification:
See spec.txt

Installation:
1) create virtual env and pip install from requirements.txt
3) set the FLASK_APP env variable and run the server with: 'export FLASK_APP=service.py; flask run'
4) send a post request to 'http://127.0.0.1:5000' with a json payload like below.
5) tests can be run from the root directory with 'python -m pytest'


EXAMPLE JSON BODY:
{
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
