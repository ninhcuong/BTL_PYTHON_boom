import math
def Check(n):
  kt=True
  if n<2:
    kt=False
  for i in range(2,int(math.sqrt(n)+1),1):
     if (n%i)==0:
        kt=False
  return kt
 
t=int(input())
for i in range(t):
    a=int(input())
    sum=0
    for i in range(1,a,1):
        if math.gcd(i,a)==1 :
            sum+=1 
        else:
            continue
    print("YES") if Check(sum) else print("NO")         
           


      