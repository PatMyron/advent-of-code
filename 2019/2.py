import os
import requests
import requests_cache
import sys

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/2019/day/2/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()
list = list(map(int, s.split(',')))

list[1] = 12
list[2] = 2
i = 0
while True:
    if list[i] == 99:
        print(list[0])
        sys.exit()
    if list[i] == 1:
        list[list[i+3]] = list[list[i+1]] + list[list[i+2]]
        i += 4
    if list[i] == 2:
        list[list[i+3]] = list[list[i+1]] * list[list[i+2]]
        i += 4
