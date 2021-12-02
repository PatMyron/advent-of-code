import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
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
