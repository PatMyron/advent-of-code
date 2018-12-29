from collections import defaultdict
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

maximum = 0
dic = defaultdict(lambda: 0)
op = {"inc": "+=", "dec": "-="}
for line in s.splitlines():
    arr = line.split()
    if eval(str(dic[arr[4]]) + arr[5] + arr[6]):
        exec("dic['" + arr[0] + "']" + op[arr[1]] + arr[2])
    if max(dic.values()) > maximum:
        maximum = max(dic.values())
print(max(dic.values()))
print(maximum)
