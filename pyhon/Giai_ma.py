import re
for i in range (int(input())):
    s=input()
    so=list(map(int,re.findall("\d",s)))
    chu=list(re.findall("\D",s))
    for i in range(len(so)):
         for j in range (so[i]):
              print(chu[i],end='')
    print()

  