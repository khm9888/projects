import sys

input = sys.stdin.readline

x = int(input())
d = 2

primes = []

while d<=x:
    if x%d==0:
        print(d)
        primes.append(d)
        x = x//d
    else:
        d=d+1

# print(primes)

