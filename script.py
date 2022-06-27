import requests

response = requests.get("https://catfact.ninja/breeds?limit=10")
responseJson = response.json()
for data in responseJson['data']:
    print(data['country'])
