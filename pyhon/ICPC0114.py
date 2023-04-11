import math
def check(n):
    kt=True
    if(n<2 ) :kt=False
    for i in range (2,int(math.sqrt(n)),1):
        if(n%i)==0: kt=False
    return kt
def kt(s):
    kt=True
    sum=0
    a=s[::-1]
    if(not check(int(a))):
        kt=False
    for i in range(len(s)):
        if(not check(int(s[i]))):
            kt=False
        else :
            sum+=int(s[i])
    if(not check(sum)) : kt=False
    return kt
for i in range (int(input())):
    a=input()
    print("Yes") if(kt(a)) else print("No")


     