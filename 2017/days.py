import math
from collections import defaultdict
import re
import numpy as np
import os
import requests
import requests_cache

requests_cache.install_cache('../cache')

# day 2

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/2/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text
sum = 0
for line in s.splitlines():
    sum += max(map(int, line.split())) - min(map(int, line.split()))
print(sum)

sum = 0
for line in s.splitlines():
    splitLine = list(map(int, line.split()))
    for i in range(len(splitLine)):
        num = splitLine[i]
        for other in splitLine[i+1:]:
            if num % other == 0:
                sum += num / other
            if other % num == 0:
                sum += other / num
print(sum)

# day 3


def round_down_to_odd(f):
    return np.ceil(f) // 2 * 2 - 1


n = 289326
squareRootOfPreviousCorner = round_down_to_odd(math.sqrt(n))
numbersInFourthOfCurrentSpiral = squareRootOfPreviousCorner + 1
previousCornerNum = squareRootOfPreviousCorner ** 2
remainder = n - previousCornerNum
remainderModded = remainder % numbersInFourthOfCurrentSpiral
answer = numbersInFourthOfCurrentSpiral - 1   # start @ startingNumberInSequence

for i in range(1, int(remainderModded)):
    if i >= numbersInFourthOfCurrentSpiral//2:
        answer += 1
    else:
        answer -= 1

print(answer)

n = 289326
m = {(0, 0): 1}
spot = (1, 0)

if (0, 1) not in m:
    print("suh")

# day 4

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/4/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text


def goodPass(line):
    for i in range(len(line.split())):
        word = line.split()[i]
        for other in line.split()[i + 1:]:
            if sorted(word) == sorted(other):
                return False
    return True


sum = 0
for line in s.splitlines():
    if goodPass(line):
        sum += 1
print(sum)

# day 5

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/5/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text
lines = list(map(int, s.splitlines()))
current, jumps = 0, 0
while current in range(0, len(lines)):
    jumps += 1
    old = current
    current += lines[current]
    if lines[old] < 3:
        lines[old] += 1
    else:
        lines[old] -= 1
print(jumps)

# day 6

s = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
l = list(map(int, s.split()))


def doRound(l):
    maxIndex = l.index(max(l))
    maxValue = max(l)
    l[maxIndex] = 0
    for i in range(maxValue):
        l[(maxIndex+1+i) % len(l)] += 1


stored = []
count = 0
while True:
    stored.append(list(l))
    doRound(l)
    count += 1
    if l in stored:
        print(count - stored.index(l))
        break

# day 7

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/7/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text


def clean(s):
    return s.replace('(', '').replace(')', '')


numberOfOccurences, tree = {}, {}
for line in s.splitlines():
    line = line.replace(',', '').split(' ')
    tree[line[0]] = line
    for elem in line:
        if "->" not in elem and "(" not in elem:
            numberOfOccurences[elem] = numberOfOccurences.get(elem, 0) + 1
print(min(numberOfOccurences, key=numberOfOccurences.get))

for node in tree[min(numberOfOccurences, key=numberOfOccurences.get)][3:]:
    print(node + str(tree[node][1:]) + clean(tree[node][1]))

# day 8

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/8/input'
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

# day 9

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/9/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text

s = re.sub("!.", '', s)
lengthOfString9before = len(s)
groupsRemoved = len(re.findall("<.*?>", s))
s = re.sub("<.*?>", '', s)
print(lengthOfString9before - len(s) - 2 * groupsRemoved)  # part 2
s = re.sub(",", '', s)
sum = 0
level = 1
for c in s:
    if c == '{':
        sum += level
        level += 1
    if c == '}':
        level -= 1
print(sum)

# day 11

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/11/input'
input11 = requests.get(url, cookies={"session": os.environ['SESSION']}).text

s = input11.split(',').count('s')-input11.split(',').count('n')
ne = input11.split(',').count('ne')-input11.split(',').count('sw')
se = input11.split(',').count('se')-input11.split(',').count('nw')

print(ne + se)

# day 12

url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/12/input'
in12 = requests.get(url, cookies={"session": os.environ['SESSION']}).text

seen = {0}
lines = in12.splitlines()


def recursion(number):
    seen.add(number)
    for n in lines[number].split(' <-> ')[1].split(', '):
        if int(n) not in seen:
            recursion(int(n))


recursion(0)
print(len(seen))
