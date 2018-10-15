s = '''set b 67
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''

dictionary = {}

for c in 'abcdefgh':
    dictionary[c] = 0

lines = s.splitlines()
mul = 0
line = 0

while line < len(lines):
    command = lines[line].split()[0]
    x = lines[line].split()[1]
    y = lines[line].split()[2]
    if y.isalpha():
        y = dictionary[y]
    else:
        y = int(y)
    if command == 'set':
        dictionary[x] = y
    if command == 'sub':
        dictionary[x] -= y
    if command == 'mul':
        mul += 1
        dictionary[x] *= y
    if command == 'jnz':
        if x.isalpha():
            x = dictionary[x]
        else:
            x = int(x)
        if x != 0:
            line += y - 1
    line += 1

print(mul)
