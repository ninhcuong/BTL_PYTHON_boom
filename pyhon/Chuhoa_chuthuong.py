import re
s=input()
x=re.findall("[A-Z]",s)
i=re.findall("[a-z]",s)
print(s.lower()) if len(i)>=len(x) else print(s.upper())