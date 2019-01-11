from collections import defaultdict
from dateutil import parser
from datetime import timedelta
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

guards = {}
wakes = defaultdict(list)
falls = defaultdict(list)

for line in s.splitlines():
    day = line.split()[0].strip('[')
    if line.split()[1].strip(']').split(':')[0] == "23":  # who shows up early to work
        day = (parser.parse(day) + timedelta(days=1)).strftime('%Y-%m-%d')
    minutes = line.split()[1].strip(']').split(':')[1]
    other = line.split()[3].strip('#')
    if other == 'up':
        wakes[day].append(minutes)
    elif other == 'asleep':
        falls[day].append(minutes)
    else:
        guards[day] = other

maxTimeAsleep = 0
for guard in set(guards.values()):
    timeAsleep = 0
    if timeAsleep > maxTimeAsleep:
        maxTimeAsleep = timeAsleep
        maxGuard = guard
