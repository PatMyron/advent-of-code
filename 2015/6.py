from collections import defaultdict
import os
import requests
import requests_cache

requests_cache.install_cache('cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

matrix = defaultdict(lambda: defaultdict(lambda: 0))

for line in s.splitlines():
    start = list(map(int, line.split()[-3].split(',')))
    end = list(map(int, line.split()[-1].split(',')))
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if "toggle" in line:
                matrix[x][y] += 2
            if "off" in line:
                matrix[x][y] = max(matrix[x][y] - 1, 0)
            if "on" in line:
                matrix[x][y] += 1

total = 0
for i in range(1000):
    for j in range(1000):
        total += matrix[i][j]
print(total)
