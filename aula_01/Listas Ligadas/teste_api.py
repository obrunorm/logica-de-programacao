import requests

response = requests.get("https://api.thecatapi.com/v1/images/search")
data = response.json()

print(data)
