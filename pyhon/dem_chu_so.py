import math
from collections import deque

def snt(a):
    if a<2: return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0: return 0
    return 1


n = int(input())
a = [int(i) for i in input().split()]
max = 0
for num in a:
    s = 0
    q = deque()
    if (snt(num)==1):
        continue
    else:
        q.append(num-1)
        q.append(num+1)
        s+=1
        while (1):
            tmp = q[0]
            q.append(tmp-1)
            q.popleft()
            if (snt(tmp)==1): break
            tmp = q[0]
            q.append(tmp+1)
            q.popleft()
            if (snt(tmp)==1): break
            s+=1
    
    if (s>max): max=s
print(max)