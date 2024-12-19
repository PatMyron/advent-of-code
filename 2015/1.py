import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

print(s.count('(') - s.count(')'))

level = 0
index = 0
while level >= 0:
    if s[index] == '(':
        level += 1
    else:
        level -= 1
    index += 1
print(index)
