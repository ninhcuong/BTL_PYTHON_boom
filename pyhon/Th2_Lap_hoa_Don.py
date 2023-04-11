n = int(input())
bills = []
for i in range(n):
    code = input()
    name = input()
    quantity = int(input())
    unit_price = int(input())
    discount = int(input())

    total_price = unit_price * quantity - discount

    bills.append((code, name, quantity, unit_price, discount, total_price))

bills.sort(key=lambda x: -x[5])

for bill in bills:
    print(*bill)