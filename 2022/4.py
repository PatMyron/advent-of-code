import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sum = 0
for line in s.splitlines():
    ids = list(map(int, line.replace(',', '-').split('-')))
    if ids[0] <= ids[2] and ids[1] >= ids[3] or ids[2] <= ids[0] and ids[3] >= ids[1]:
        sum += 1
print(sum)
