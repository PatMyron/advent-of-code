import re
import os
import requests
import requests_cache

requests_cache.install_cache('cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

values = {}
for line in s.splitlines():
    if re.match(r'\d+ -', line):
        values[str(line.split('->')[1].strip())] = int(line.split('->')[0])

print(values)
