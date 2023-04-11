s=input()
k=s
check=0
for i in range(-3,-len(s),-3):  
      k=s[:i]+","+k[i-check:]
      check+=1
      print(k)
print(k)