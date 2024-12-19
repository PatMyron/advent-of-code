import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()


def clean(s):
    return s.replace('(', '').replace(')', '')


numberOfOccurrences, tree = {}, {}
for line in s.splitlines():
    line = line.replace(',', '').split(' ')
    tree[line[0]] = line
    for elem in line:
        if "->" not in elem and "(" not in elem:
            numberOfOccurrences[elem] = numberOfOccurrences.get(elem, 0) + 1
print(min(numberOfOccurrences, key=numberOfOccurrences.get))

for node in tree[min(numberOfOccurrences, key=numberOfOccurrences.get)][3:]:
    print(node + str(tree[node][1:]) + clean(tree[node][1]))
