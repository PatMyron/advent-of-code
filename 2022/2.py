import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}
sum = 0
for line in s.splitlines():
    mod = (values[line.split()[1]] - values[line.split()[0]] + 1) % 3
    sum += 3 * mod + values[line.split()[1]]
print(sum)
