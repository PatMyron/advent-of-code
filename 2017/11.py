import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

so = s.split(',').count('s') - s.split(',').count('n')
ne = s.split(',').count('ne') - s.split(',').count('sw')
se = s.split(',').count('se') - s.split(',').count('nw')

print(ne + se)

maximum = 0
for i in range(len(s.split(','))):
    so = abs(s.split(',')[:i + 1].count('s') - s.split(',')[:i + 1].count('n'))
    ne = abs(s.split(',')[:i + 1].count('ne') - s.split(',')[:i + 1].count('sw'))
    se = abs(s.split(',')[:i + 1].count('se') - s.split(',')[:i + 1].count('nw'))
    maximum = max(maximum, ne + se)
print(maximum)
