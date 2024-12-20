import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

dictionary = {}

for c in 'abcdefgh':
    dictionary[c] = 0

# part 2
# dictionary['a'] = 1

lines = s.splitlines()
mul = 0
line = 0

while line < len(lines):
    command = lines[line].split()[0]
    x = lines[line].split()[1]
    y = lines[line].split()[2]
    if y.isalpha():
        y = dictionary[y]
    else:
        y = int(y)
    if command == 'set':
        dictionary[x] = y
    if command == 'sub':
        dictionary[x] -= y
    if command == 'mul':
        mul += 1
        dictionary[x] *= y
    if command == 'jnz':
        if x.isalpha():
            x = dictionary[x]
        else:
            x = int(x)
        if x != 0:
            line += y - 1
    line += 1

print(mul)
