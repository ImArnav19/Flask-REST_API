import requests
BASE = 'http://127.0.0.1:5000/'

resp = requests.post(BASE + 'hw/19',{"likes":10, "name": "ManlyBadassZero!!", "views" : 10000,})

obj = resp
print(obj.json())
input()
resp = requests.get(BASE + 'hw/19')
print(resp.json())

input()
resp = requests.delete(BASE + 'hw/19')
print(resp.json())



