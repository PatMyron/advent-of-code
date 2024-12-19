import hashlib
import sys
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

for i in range(sys.maxsize):
    if hashlib.md5((s + str(i)).encode()).hexdigest().startswith("000000"):
        print(i)
        exit()
