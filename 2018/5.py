import sys
import os
import requests
import requests_cache
import multiprocessing

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input5 = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sys.setrecursionlimit(40000)  # sorry


def recursion(s, lowered):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1] and lowered[i] == lowered[i + 1]:
            s = s[:i] + s[i + 2 :]
            lowered = lowered[:i] + lowered[i + 2 :]
            return recursion(s, lowered)
    return s


part1 = recursion(input5, input5.lower())
print(len(part1))


def removingLetter(char):
    iteration = part1.replace(chr(char), '').replace(chr(char).upper(), '')
    return len(recursion(iteration, iteration.lower()))


print(min(multiprocessing.Pool().map(removingLetter, range(ord('a'), ord('z') + 1))))
