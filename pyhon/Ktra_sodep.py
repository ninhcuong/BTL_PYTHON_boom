def check(a):
      kt=True
      if a[0]==a[1] :kt=False
      for i in range(len(a)-2): 
        if a[i]!=a[i+2] : kt=False
      return kt

for i in range (int(input())): 
    a=input()
    print("YES") if(check(a)) else print("NO")
    