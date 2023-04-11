import math
def check(a): 
    sum=0
    if(a%2)==0:
         for i in range(2,a+1,2): 
              sum+=float(1/i)
    else : 
           for i in range(1,a+1,2): 
              sum+=float(1/i)
    result=format(sum,'.6f')
    return result
for i in range (int(input())): 
    a=int(input())
    print(check(a))
