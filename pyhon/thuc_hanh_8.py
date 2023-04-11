def find_partitions(n):
    # Nếu n = 1, chỉ có một cách biểu diễn là n = 1
    if n == 1:
        return [[1]]
    
    # Nếu n > 1, tìm tất cả các cách biểu diễn n-1
    prev_partitions = find_partitions(n-1)
    
    # Thêm số 1 vào mỗi cách biểu diễn n-1 để tạo ra tất cả các cách biểu diễn n
    partitions = []
    for partition in prev_partitions:
        partitions.append(partition + [1])
    
    # Tìm tất cả các cách biểu diễn n có 2 số trở lên
    for i in range(n-1, 0, -1):
        for partition in find_partitions(i):
            if partition[-1] <= n-i:
                partitions.append(partition + [n-i])
    
    return partitions

# Nhập số lượng test
t = int(input())

for i in range(t):
    # Nhập giá trị N
    n = int(input())
    
    # Tìm tất cả các cách biểu diễn N và in ra kết quả
    partitions = find_partitions(n)
    print(len(partitions))
    for partition in partitions:
        print(*partition)