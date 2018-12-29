a = 873
b = 583

af = 16807
bf = 48271

mod = 2147483647
sum = 0

for i in range(40000000):
    a = a * af % mod
    b = b * bf % mod
    if a % 2**16 == b % 2**16:
        sum += 1

print(sum)
