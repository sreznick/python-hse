import requests

resp = requests.get('https://yandex.ru')
print(bool(resp))
print(resp.ok)
resp = requests.get('https://yandex.ru/dwdwcqw')
print(bool(resp))
print(resp.ok)

