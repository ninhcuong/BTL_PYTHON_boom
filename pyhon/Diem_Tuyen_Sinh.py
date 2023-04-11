import math

n = int(input())
a = list(map(int, input().split()))

gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a[i])

sum_b = sum([a[i] // gcd for i in range(n-1)])
print(sum_b)