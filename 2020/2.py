import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

total = 0
for line in s.splitlines():
    num = line.split()[0].split('-')
    letter = line.split()[1].split(':')[0]
    if (line.split()[2][int(num[0]) - 1] == letter) ^ (line.split()[2][int(num[1]) - 1] == letter):
        total += 1
print(total)
