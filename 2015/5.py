import re
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

total = 0
for line in s.splitlines():
    if re.search(r'(\w)(\w).*\1\2', line) and re.search(r'(\w)\w\1', line):
        total += 1
print(total)
