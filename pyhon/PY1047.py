import math
def check(a):  
    kt=True
    if(a<2 ) : kt=False
    for i in range(2,int(math.sqrt(a))+1,1): 
        if(a%i)==0: 
            kt=False
            break
    return kt
def kt(s):
    kt=True
    if check(len(s)) : 
        kt=True
    else :
         kt=False
    dem=0
    for i in range(len(s)): 
        if(check(int(s[i]))) :
             dem+=1
    if len(s)-dem>=dem  :
         kt=False
    return kt
     
for i in range(int(input())):
     a=input()
     print("YES") if(kt(a)) else print("NO")
     
     