import requests
import json

# your server information 
serverip = "play.spaffel.de"
# if you have no special Port dont change this
port = "25565"





headers = {"ip": serverip, "port": port}

#dont change this url
url = "http://hosting.spaffel.de:25578/getdata"

s = requests.Session()
s.headers.update(headers)
response = requests.post(url, headers = headers)

response = json.loads(response.text)

playercount = response["players"]
ping = response["ping"]

print(f"Players: {playercount}")
print(f"Ping: {ping}")
