import hashlib
import sys
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

for i in range(sys.maxsize):
    if hashlib.md5((s + str(i)).encode()).hexdigest().startswith("000000"):
        print(i)
        exit()
