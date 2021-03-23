import requests

url = "http://127.0.0.1:8000/greetings/Your_name"

headers = {'authentication' : "test_code"}
payload = {"item" : "test_item"}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.status_code)
print(response.text)