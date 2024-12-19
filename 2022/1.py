import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

maximum = 0
current = 0
for line in s.splitlines():
    if line == '':
        current = 0
    else:
        current += int(line)
        maximum = max(current, maximum)
print(maximum)
