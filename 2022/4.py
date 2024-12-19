import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for line in s.splitlines():
    ids = list(map(int, line.replace(',', '-').split('-')))
    if ids[0] <= ids[2] and ids[1] >= ids[3] or ids[2] <= ids[0] and ids[3] >= ids[1]:
        sum += 1
print(sum)
