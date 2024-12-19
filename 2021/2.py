import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

x, y, aim = 0, 0, 0
for line in s.splitlines():
    if line.startswith('forward'):
        y += aim * int(line.split()[1])
        x += int(line.split()[1])
    if line.startswith('up'):
        aim -= int(line.split()[1])
    if line.startswith('down'):
        aim += int(line.split()[1])
print(x*y)
