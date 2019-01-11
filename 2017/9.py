import re
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
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
