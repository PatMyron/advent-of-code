import math
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

totalPaper = 0
totalRibbon = 0
for line in s.splitlines():
    numbers = list(map(int, line.split('x')))
    product = math.prod(numbers)
    totalRibbon += product + 2 * sum(sorted(numbers)[:2])
    numbers = [product // x for x in numbers]
    totalPaper += min(numbers) + 2 * sum(numbers)
print(totalPaper)
print(totalRibbon)
