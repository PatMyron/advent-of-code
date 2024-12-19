import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

visited = set()
x = [0, 0]
y = [0, 0]
i = 0
for move in s:
    visited.add("0,0")
    if move == '>':
        x[i] += 1
    if move == '<':
        x[i] -= 1
    if move == '^':
        y[i] += 1
    if move == 'v':
        y[i] -= 1
    visited.add(str(x[0]) + "," + str(y[0]))
    visited.add(str(x[1]) + "," + str(y[1]))
    i = int(not i)
print(len(visited))
