from collections import defaultdict
import string
import os
import requests
import requests_cache

requests_cache.install_cache('cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

prereqs = defaultdict(list)

for line in s.splitlines():
    prereqs[line.split()[7]].append(line.split()[1])
while True:
    for letter in string.ascii_uppercase:
        if not prereqs[letter]:
            print(letter, end='')
            prereqs[letter].append('DONE')
            for prereq in prereqs.values():
                if letter in prereq:
                    prereq.remove(letter)
            break
