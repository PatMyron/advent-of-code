import re
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input5 = requests.get(url, cookies={"session": os.environ['SESSION']}).text

total = 0
for line in input5.splitlines():
    if re.search(r'(\w)(\w).*\1\2', line) and re.search(r'(\w)\w\1', line):
        total += 1
print(total)
