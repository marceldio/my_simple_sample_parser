import requests

url = "https://parsinger.ru/3.4/2/index.html"
response = requests.get(url)
response.encoding="utf-8"
print(response.text)
