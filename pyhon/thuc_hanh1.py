
n = int(input())
sv = []
class Thisinh:
    def __init__(self, msv, name, lop, cc, note) -> None:
        self.msv = msv
        self.name = name
        self.lop = lop
        self.cc = cc
        self.note = note
    def detail(self):
        print(self.msv, self.name, self.lop, self.cc, self.note)
for _ in range(n):
    sv.append(Thisinh(input(),input(),input(),0,""))

for _ in range(n):
    s1, s2 = map(str, input().split())
    diem = 10
    for i in s2:
        if (i=='v'): diem = diem-2
        else :
            if (i=='m'):
                diem=diem-1
            
    for i in sv:
        if s1 == i.msv:
            if (diem<=0):
                i.cc = 0
                i.note = "KDDK"
            else:
                i.cc = diem
for i in sv:
    i.detail()
        