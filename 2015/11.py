import re
import string
s = 'hepxcrrq'

while True:
    for i in range(len(s) - 2):
        if s[i:i+3] in string.ascii_lowercase and re.search(r'(\w)\1', s) and not re.search(r'[iol]', s):
            print(s)
            exit()
    # base 26 equivalent of s += 1
