import hashlib
import sys

input4 = '''bgvyzdsv'''

for i in range(sys.maxsize):
    if hashlib.md5((input4 + str(i)).encode('utf-8')).hexdigest().startswith("00000"):
        print(i)
        exit()
