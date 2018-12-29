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
