import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()
lines = list(map(int, s.splitlines()))
current, jumps = 0, 0
while current in range(0, len(lines)):
    jumps += 1
    old = current
    current += lines[current]
    if lines[old] < 3:
        lines[old] += 1
    else:
        lines[old] -= 1
print(jumps)
