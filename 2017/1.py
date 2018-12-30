import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for i in range(len(s)):
    if s[i] == s[(i + len(s) // 2) % len(s)]:
        sum += int(s[i])
print(sum)
