import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/12/input'
in12 = requests.get(url, cookies={"session": os.environ['SESSION']}).text

seen = {0}
lines = in12.splitlines()


def recursion(number):
    seen.add(number)
    for n in lines[number].split(' <-> ')[1].split(', '):
        if int(n) not in seen:
            recursion(int(n))


recursion(0)
print(len(seen))
