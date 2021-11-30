import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

position = [0, 2]
map = {
    (2, 4): 1,
    (1, 3): 2,
    (2, 3): 3,
    (3, 3): 4,
    (0, 2): 5,
    (1, 2): 6,
    (2, 2): 7,
    (3, 2): 8,
    (4, 2): 9,
    (1, 1): 'A',
    (2, 1): 'B',
    (3, 1): 'C',
    (2, 0): 'D',
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
