import re
import sys
for s in sys.stdin:
    s = s.strip()
    s = re.sub("\s+"," ",s)
    s = s.strip().lower()
    s = s.capitalize()
    if s.endswith('.') or s.endswith('!') or s.endswith('?'):
        if s[len(s)-2]==" ":
            s = s.replace(" "+s[len(s)-1],''+s[len(s)-1])
    else:
        s+="."
    
    print(s)