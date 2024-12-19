import re
import string
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()


def incrementByRecursion(s, i):
    if s[i] == 'z':
        s[i] = 'a'
        incrementByRecursion(s, i - 1)
    else:
        s[i] = chr(ord(s[i]) + 1)


while True:
    for i in range(len(s) - 2):
        if s[i:i+3] in string.ascii_lowercase and re.search(r'(\w)\1.*(\w)\2', s) and not re.search(r'[iol]', s):
            print(s)
            exit()
    s = list(s)
    incrementByRecursion(s, -1)
    s = ''.join(s)
