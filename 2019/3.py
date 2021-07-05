import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
s = requests.get(url, cookies={"session": os.environ['SESSION']}).text.strip()


def allPositions(line):
    position = '0,0'
    positions = set()
    for move in line.split(','):
        # TODO cover positions during the move
        if move[0] == 'U':
            position = position.split(',')[0] + ',' + str(int(position.split(',')[1]) + int(move[1:]))
        if move[0] == 'D':
            position = position.split(',')[0] + ',' + str(int(position.split(',')[1]) - int(move[1:]))
        if move[0] == 'R':
            position = str(int(position.split(',')[0]) + int(move[1:])) + ',' + position.split(',')[1]
        if move[0] == 'L':
            position = str(int(position.split(',')[0]) - int(move[1:])) + ',' + position.split(',')[1]
        positions.add(position)
    return positions


intersection = allPositions(s.splitlines()[0]).intersection(allPositions(s.splitlines()[1]))
# print(min(map(lambda x: abs(int(x.split(',')[0])) + abs(int(x.split(',')[1])), intersection)))