import math
def check(n):
    kt=True
    if(n<2): kt=False
    for i in range (2,int(math.sqrt(n))+1,1):
         if(n%i)==0 :
            kt=False
    return kt
t=int(input())
for i in range (t):
     a,b=map(int,input().split())
     k=math.gcd(a,b)
     sum=0
     for i in str(k):
        sum+=int(i)
     print("YES") if check(sum) else print("NO")




   