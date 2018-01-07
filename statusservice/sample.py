import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {yourip}'.format(yourip=response.json()['origin']))
