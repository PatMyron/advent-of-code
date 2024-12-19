import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

for i in map(int, s.splitlines()):
    for j in map(int, s.splitlines()):
        for k in map(int, s.splitlines()):
            if i + j + k == 2020:
                print(i * j * k)
                exit()
