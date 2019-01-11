import numpy
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input2 = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

totalPaper = 0
totalRibbon = 0
for line in input2.splitlines():
    numbers = list(map(int, line.split('x')))
    product = numpy.prod(numbers)
    totalRibbon += product + 2 * sum(sorted(numbers)[:2])
    numbers = [product // x for x in numbers]
    totalPaper += min(numbers) + 2 * sum(numbers)
print(totalPaper)
print(totalRibbon)
