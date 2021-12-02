import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

x, y = 0, 0
for line in s.splitlines():
    if line.startswith('forward'):
        x += int(line.split()[1])
    if line.startswith('up'):
        y += int(line.split()[1])
    if line.startswith('down'):
        y -= int(line.split()[1])
print(x*y)
