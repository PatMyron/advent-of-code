import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text


def goodPass(line):
    for i in range(len(line.split())):
        word = line.split()[i]
        for other in line.split()[i + 1:]:
            if sorted(word) == sorted(other):
                return False
    return True


sum = 0
for line in s.splitlines():
    if goodPass(line):
        sum += 1
print(sum)
