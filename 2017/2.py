import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
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
        for other in splitLine[i+1:]:
            if num % other == 0:
                sum += num / other
            if other % num == 0:
                sum += other / num
print(sum)
