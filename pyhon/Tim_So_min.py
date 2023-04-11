import re
for i in range(int(input())):
    s=input()
    s=re.sub("\D"," ",s)
    a=list(map(int,s.split()))
    print(max(a))

