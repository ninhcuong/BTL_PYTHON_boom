a=int(input())
s=list()
check=True
while len(s)<a:
    s=[int(i) for i in input().split()]
while check:
    check=False
    for i in range (len(s)-1):
        if i>= len(s)-1 :
            break
        elif (s[i]+s[i+1]) %2==0 :
             s.pop(i)
             s.pop(i)
             i-=1
             check=True
print(len(s))


