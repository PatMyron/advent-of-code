import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()
sum1, sum2 = 0, 0
for line in map(int, s.splitlines()):
    line = line // 3 - 2
    sum1 += line
    while line > 0:
        sum2 += line
        line = line // 3 - 2
print(sum1, sum2)
