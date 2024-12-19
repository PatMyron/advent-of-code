import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

banks = list(map(int, s.split()))


def doRound(banks):
    maxIndex = banks.index(max(banks))
    maxValue = max(banks)
    banks[maxIndex] = 0
    for i in range(maxValue):
        banks[(maxIndex + 1 + i) % len(banks)] += 1


stored = []
count = 0
while True:
    stored.append(list(banks))
    doRound(banks)
    count += 1
    if banks in stored:
        print(count - stored.index(banks))
        break
