import math

def round_number(n):
    order = int(math.log10(n))
    rounding_base = 10**(order )
    return int(round(n / rounding_base) * rounding_base)

for i  in range(int(input())):
    a=int(input())
    print(round_number(a))
