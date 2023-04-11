def check(s):
    for i in range(len(s)-1):
        if(s[i])>s[i+1]:
            return False
    return True
t=int(input())
for i in range (t): 
    string=input()
    print("YES") if check(string) else print("NO")