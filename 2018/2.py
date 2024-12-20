import Levenshtein
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

two = 0
three = 0

for line in s.splitlines():
    twos = False
    threes = False
    for char in range(ord('a'), ord('z') + 1):
        if line.count(chr(char)) == 2:
            twos = True
        if line.count(chr(char)) == 3:
            threes = True
    two += int(twos)
    three += int(threes)
    for otherLine in s.splitlines():
        if Levenshtein.distance(line, otherLine) == 1:
            print(line)

print(two * three)
