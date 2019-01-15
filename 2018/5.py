import sys
import os
import requests
import requests_cache
import multiprocessing

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input5 = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()

sys.setrecursionlimit(40000)  # sorry


def recursion(s):
    for i in range(len(s) - 1):
        if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
            s = s[:i] + s[i + 2:]
            return recursion(s)
    return s


print(len(recursion(input5)))


def removingLetter(char):
    return len(recursion(input5.replace(chr(char), '').replace(chr(char).upper(), '')))


print(min(multiprocessing.Pool().map(removingLetter, range(ord('a'), ord('z') + 1))))
