import requests
import time

url = "https://httpbin.org/get"

num_requests = 100


def foo():
    start = time.time()
    for i in range(num_requests):
        requests.get(url)
    print(time.time() - start)


foo()
