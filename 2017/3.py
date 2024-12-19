import math
import os
import requests
import requests_cache
from pathlib import Path

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + Path(__file__).parent.name + '/day/' + Path(__file__).stem + '/input'
n = int(requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip())


def round_down_to_odd(f):
    return math.ceil(f) // 2 * 2 - 1


squareRootOfPreviousCorner = round_down_to_odd(math.sqrt(n))
numbersInFourthOfCurrentSpiral = squareRootOfPreviousCorner + 1
previousCornerNum = squareRootOfPreviousCorner ** 2
remainder = n - previousCornerNum
remainderModded = remainder % numbersInFourthOfCurrentSpiral
answer = numbersInFourthOfCurrentSpiral - 1  # start @ startingNumberInSequence

for i in range(1, int(remainderModded)):
    if i >= numbersInFourthOfCurrentSpiral // 2:
        answer += 1
    else:
        answer -= 1

print(answer)

n = 289326
m = {(0, 0): 1}
spot = (1, 0)

if (0, 1) not in m:
    print("suh")
