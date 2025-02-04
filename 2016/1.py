import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

x = 0
y = 0
direction = 0
moves = s.split(', ')
visited = set()
first = True
for move in moves:
    if move[0] == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    for i in range(int(move[1:])):
        if str(x) + "," + str(y) in visited and first:
            print(abs(x) + abs(y))
            first = False
        visited.add(str(x) + "," + str(y))
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
print(abs(x) + abs(y))
