import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

position = [1, 1]
map = {
    (-1, 1): 1,
    (0, 1): 2,
    (1, 1): 3,
    (-1, 0): 4,
    (0, 0): 5,
    (1, 0): 6,
    (-1, -1): 7,
    (0, -1): 8,
    (1, -1): 9,
}
for line in s.splitlines():
    for c in line:
        prev = position.copy()
        if c == 'U':
            position[1] += 1
        if c == 'D':
            position[1] -= 1
        if c == 'L':
            position[0] -= 1
        if c == 'R':
            position[0] += 1
        if tuple(position) not in map:
            position = prev.copy()
    print(map[tuple(position)], end='')
