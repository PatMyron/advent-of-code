import sys
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

count = 0
prev = sys.maxsize
for line in map(int, s.splitlines()):
    if line > prev:
        count += 1
    prev = line
print(count)
