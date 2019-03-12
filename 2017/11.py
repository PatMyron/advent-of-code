import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input11 = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

s = input11.split(',').count('s') - input11.split(',').count('n')
ne = input11.split(',').count('ne') - input11.split(',').count('sw')
se = input11.split(',').count('se') - input11.split(',').count('nw')

print(ne + se)

maximum = 0
for i in range(len(input11.split(','))):
    s = abs(input11.split(',')[:i+1].count('s')-input11.split(',')[:i+1].count('n'))
    ne = abs(input11.split(',')[:i+1].count('ne')-input11.split(',')[:i+1].count('sw'))
    se = abs(input11.split(',')[:i+1].count('se')-input11.split(',')[:i+1].count('nw'))
    maximum = max(maximum, ne + se)
print(maximum)
