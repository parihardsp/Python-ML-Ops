import json
import requests

# Passing parameters as query parameters as they go in headers.
url = 'http://127.0.0.1:8000/orders'

headers = {
    'accept': 'application/json'
}

params = {
    'product': 'laptop',
    'units': '10'
}

response = requests.post(url, headers=headers, params=params)

print(response.json())

'''
Result: 
curl -X 'POST' \
  'http://127.0.0.1:8000/orders?product=laptop&units=10' \
  -H 'accept: application/json' \
  -d ''
  
http://127.0.0.1:8000/orders?product=laptop&units=10 
'''

# Passing parameters as body as they go in body.
url = 'http://127.0.0.1:8000/orders-pydantic'

headers = {
    'accept': 'application/json',
    'Content-type': 'application/json'
}

params = {
    'product': 'laptop-new',
    'units': '10'
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.json())

'''
Result: 
curl -X 'POST' \
  'http://127.0.0.1:8000/orders-pydantic' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "product": "laptop-new",
  "units": 10
}'
http://127.0.0.1:8000/orders-pydantic
'''
