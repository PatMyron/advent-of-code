import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for line in s.splitlines():
    for ch in set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:])):
        if ch.islower():
            sum += ord(ch) - 96
        else:
            sum += ord(ch) - 38
print(sum)
