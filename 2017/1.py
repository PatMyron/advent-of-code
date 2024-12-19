import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for i in range(len(s)):
    if s[i] == s[(i + len(s) // 2) % len(s)]:
        sum += int(s[i])
print(sum)
