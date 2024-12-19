import re
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

s = re.sub("!.", '', s)
lengthOfString9before = len(s)
groupsRemoved = len(re.findall("<.*?>", s))
s = re.sub("<.*?>", '', s)
print(lengthOfString9before - len(s) - 2 * groupsRemoved)  # part 2
s = re.sub(",", '', s)
sum = 0
level = 1
for c in s:
    if c == '{':
        sum += level
        level += 1
    if c == '}':
        level -= 1
print(sum)
