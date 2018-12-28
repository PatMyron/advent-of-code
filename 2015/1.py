import os
import requests
import requests_cache

requests_cache.install_cache('cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

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
