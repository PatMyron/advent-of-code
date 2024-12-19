from collections import defaultdict
import string
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

prereqs = defaultdict(list)

for line in s.splitlines():
    prereqs[line.split()[7]].append(line.split()[1])
while not all(array == ['DONE'] for array in prereqs.values()):
    for letter in string.ascii_uppercase:
        if not prereqs[letter]:
            print(letter, end='')
            prereqs[letter].append('DONE')
            for prereq in prereqs.values():
                if letter in prereq:
                    prereq.remove(letter)
            break
