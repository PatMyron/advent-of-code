import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

seen = {0}
lines = s.splitlines()


def recursion(number):
    seen.add(number)
    for n in lines[number].split(' <-> ')[1].split(', '):
        if int(n) not in seen:
            recursion(int(n))


recursion(0)
print(len(seen))
