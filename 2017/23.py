import os
import requests
import requests_cache

requests_cache.install_cache('cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

dictionary = {}

for c in 'abcdefgh':
    dictionary[c] = 0

dictionary['a'] = 1

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
