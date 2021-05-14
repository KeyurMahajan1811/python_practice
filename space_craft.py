import requests

responce = requests.get("http://api.open-notify.org/astros.json")

json = responce.json()

for key in json["people"]:
    print(key["name"])


print(json)
