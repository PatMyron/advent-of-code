import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

total = 0
for line in s.splitlines():
    num = line.split()[0].split('-')
    letter = line.split()[1].split(':')[0]
    if int(num[0]) <= line.split()[2].count(letter) <= int(num[1]):
        total += 1
print(total)
