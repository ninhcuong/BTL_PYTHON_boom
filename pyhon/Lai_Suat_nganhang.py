import math
t=int(input())
for i in range(t) :
     a,b,c = map(float,input().split())
     c=c/a
     b=1+b/100
     c=math.log(c,b)
     print(c) if isinstance(c,int) else print(math.ceil(c))

