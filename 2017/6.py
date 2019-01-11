import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

l = list(map(int, s.split()))


def doRound(l):
    maxIndex = l.index(max(l))
    maxValue = max(l)
    l[maxIndex] = 0
    for i in range(maxValue):
        l[(maxIndex+1+i) % len(l)] += 1


stored = []
count = 0
while True:
    stored.append(list(l))
    doRound(l)
    count += 1
    if l in stored:
        print(count - stored.index(l))
        break
