t=input()
def check(a):
 b = a.copy()
 b.sort()
 l = len(b)
 if len(b)%2!=0:
    k=int(len(b)/2)
 else: 
    k1 = a.index(b[int(l/2)-1])
    k2 = a.index(b[int(l/2)])
    if k1 < k2: k= int(l/2) -1
    else: k = int(l/2)
 s1 = 0
 s2 = 0
 for i in range(0,k):
    s1 = s1+b[i]
 for i in range(k+1,l):
    s2 = s2+b[i]
 s = b[k]*(k) - s1 + s2 - b[k]*(l-k-1)
 print(s,b[k]) 
a = [int(i) for i in input().split()]
check(a)


