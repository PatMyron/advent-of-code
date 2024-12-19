import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

print(sum(map(int, s.splitlines())))

seen = set()
current = 0
while True:
    for line in map(int, s.splitlines()):
        seen.add(current)
        current += line
        if current in seen:
            print(current)
            exit()
