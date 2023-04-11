import math
def check(a):  
    kt=True
    if(a<2 ) : kt=False
    for i in range(2,int(math.sqrt(a))+1,1): 
        if(a%i)==0: 
            kt=False
            break
    return kt
for i in range (int(input())): 
     a=input()
     b=int(a[-4:])
     print("YES") if(check(b)) else print("NO")