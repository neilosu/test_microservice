import requests
import json

url = "http://127.0.0.1:5000/db/acquire_unit"

payload = json.dumps({
  "list": 1,
  "unit": 6,
  "attribute": [
    "word",
    "sentence"
  ]
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, timeout=10)

result = response.json()
result_dict = json.loads(result)

print(json.dumps(result_dict, indent=4))

