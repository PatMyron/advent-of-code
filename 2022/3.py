import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for line in s.splitlines():
    for ch in set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:])):
        if ch.islower():
            sum += ord(ch) - 96
        else:
            sum += ord(ch) - 38
print(sum)
