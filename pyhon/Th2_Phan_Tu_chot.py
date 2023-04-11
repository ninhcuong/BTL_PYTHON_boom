def count_pivots(arr, n):
    count = 0
    max_left = -1
    for i in range(n):
        if arr[i] >= max_left:
            max_right = max(arr[i+1:]) if i < n-1 else -1
            if arr[i] > max_right:
                count += 1
            max_left = arr[i]
    return count

# Hàm main
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_pivots(arr, n))