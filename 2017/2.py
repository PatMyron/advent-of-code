import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()
sum = 0
for line in s.splitlines():
    sum += max(map(int, line.split())) - min(map(int, line.split()))
print(sum)

sum = 0
for line in s.splitlines():
    splitLine = list(map(int, line.split()))
    for i in range(len(splitLine)):
        num = splitLine[i]
        for other in splitLine[i + 1:]:
            if num % other == 0:
                sum += num / other
            if other % num == 0:
                sum += other / num
print(sum)
