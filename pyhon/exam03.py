MOD = 10**9 + 7

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x % MOD, n // 2)
    else:
        return power(x * x % MOD, n // 2) * x % MOD

def inverse(x):
    return power(x, MOD-2)

t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    s = 0
    for i in range(k+1):
        num = (power(n, i+1) - power(n-1, i+1)) % MOD
        den = (i+1) % MOD
        s = (s + num * inverse(den)) % MOD
    print(s)