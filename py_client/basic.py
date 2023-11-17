import requests

# endpoint = "http://www.httpbin.org"
endpoint = "http://127.0.0.1:8000/"

# GET
response = requests.get(endpoint)
print(response.status_code)