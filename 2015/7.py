import re
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

values = {}
for line in s.splitlines():
    if re.match(r'\d+ -', line):
        values[str(line.split('->')[1].strip())] = int(line.split('->')[0])

print(values)
