
def check(n, lst=[]):
    if n == 0:
        # print(lst)
        return 1
    count = 0
    start = 1 if not lst else lst[-1]
    for i in range(start, n+1):
        count += check(n-i, lst + [i])
    return count
def ins(n, a):
    print("(", end="")
    for i in range(1, n):
        print(a[i], end=" ")
    print(a[n], end="")
    print(") ", end="")

def quaylui2(n, i, s, a):
    for j in range(n, 0, -1):
        a[i] = j
        if j == s:
            ins(i, a)
        elif j < s:
            quaylui2(j, i+1, s-j, a)

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    a = [0] * 50
    
    print(check(n))
    quaylui2(n, 1, n, a)
    
