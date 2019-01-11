from collections import defaultdict
import re
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

matrix = defaultdict(lambda: defaultdict(lambda: 0))

for line in s.splitlines():
    numbers = list(map(int, re.split('[,x:@]', line.split('#')[1])))
    for x in range(numbers[1], numbers[1] + numbers[3]):
        for y in range(numbers[2], numbers[2] + numbers[4]):
            matrix[x][y] += 1

total = 0
for i in range(1000):
    for j in range(1000):
        if matrix[i][j] > 1:
            total += 1
print(total)

for line in s.splitlines():
    numbers = list(map(int, re.split('[,x:@]', line.split('#')[1])))
    covered = False
    for x in range(numbers[1], numbers[1] + numbers[3]):
        for y in range(numbers[2], numbers[2] + numbers[4]):
            if matrix[x][y] > 1:
                covered = True
    if not covered:
        print(numbers[0])
