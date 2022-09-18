# 삽입 정렬

arr = [7,5,9,0,3,1,6,2,4,8]

N = len(arr)

# 1
# 0

# 2
# 1 0

# 3
# 2 1 0

#...

# N-1
# N-2 N-3 ... 0

for i in range(1, N):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)