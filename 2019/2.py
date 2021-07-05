import os
import requests
import requests_cache
import sys

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

for noun in range(100):
    for verb in range(100):
        l = list(map(int, s.split(',')))
        l[1] = noun
        l[2] = verb
        i = 0
        while True:
            if l[i] == 99:
                if l[0] == 19690720:
                    print(100 * noun + verb)
                    sys.exit()
                break
            elif l[i] == 1:
                l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
                i += 4
            elif l[i] == 2:
                l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
                i += 4
