import sys
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

count = 0
for i in range(len(s.splitlines())):
    if i < 3:
        continue
    elif list(map(int, s.splitlines()))[i] > list(map(int, s.splitlines()))[i-3]:
        count += 1
print(count)
