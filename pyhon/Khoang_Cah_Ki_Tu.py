import math
def check(a):
    s=list(a)
    s1=s[::-1]
    for i in range(len(s1)):
        if(abs(ord(s[i])-ord(s[i-1]))!=(abs(ord(s1[i])-ord(s1[i-1])))):
          return False
    return True
for i in range (int(input())): 
     a=input()
     print("YES") if(check(a)) else print("NO")
      