import requests

url = 'http://httpbin.org/ip'


proxies = {
    'http': 'http://188.133.200.60:8081',
    'https': 'https://188.133.200.60:8081',
}


response = requests.get(url, proxies=proxies)

print(response.json())
