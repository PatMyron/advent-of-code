import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

a = int(s.splitlines()[0].split()[-1])
b = int(s.splitlines()[1].split()[-1])

af = 16807
bf = 48271

mod = 2147483647
sum = 0

for i in range(40000000):
    a = a * af % mod
    b = b * bf % mod
    if a % 2 ** 16 == b % 2 ** 16:
        sum += 1

print(sum)
