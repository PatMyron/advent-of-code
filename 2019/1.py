import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()
sum1, sum2 = 0, 0
for line in map(int, s.splitlines()):
    line = line // 3 - 2
    sum1 += line
    while line > 0:
        sum2 += line
        line = line // 3 - 2
print(sum1, sum2)
