import math
def check(s) : 
    s1=s[::-1]
    x=math.gcd(int(s),int(s1))
    if x==1:
         return True
    else :
         return False
for i in range (int(input())): 
    s=input()
    print("YES") if check(s) else print("NO")