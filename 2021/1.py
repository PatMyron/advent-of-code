import sys
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

count = 0
for i in range(len(s.splitlines())):
    if i < 3:
        continue
    elif list(map(int, s.splitlines()))[i] > list(map(int, s.splitlines()))[i-3]:
        count += 1
print(count)
