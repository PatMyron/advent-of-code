import re
import string
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

while True:
    for i in range(len(s) - 2):
        if s[i:i+3] in string.ascii_lowercase and re.search(r'(\w)\1', s) and not re.search(r'[iol]', s):
            print(s)
            exit()
    # base 26 equivalent of s += 1
