import requests
from random import choice

url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent, timeout=2)
    print(response.text)

# Выполнение GET-запроса с установленными заголовками
response = requests.get('http://httpbin.org/user-agent', headers=headers)

print(response.text)


# >>> {
#        "user-agent": "Mozilla/5.0"
#     }