import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

maximum = 0
current = 0
for line in s.splitlines():
    if line == '':
        current = 0
    else:
        current += int(line)
        maximum = max(current, maximum)
print(maximum)
