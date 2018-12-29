import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

x = 0
y = 0
direction = 0
moves = s.split(', ')
for move in moves:
    if move[0] == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    if direction == 0:
        y += int(move[1:])
    elif direction == 1:
        x += int(move[1:])
    elif direction == 2:
        y -= int(move[1:])
    elif direction == 3:
        x -= int(move[1:])

print(abs(x) + abs(y))
