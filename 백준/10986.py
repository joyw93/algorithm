inputs = list(map(int, input().split()))

N = inputs[0]
M = inputs[1]

count = 0
nums = list(map(int, input().split()))

def mod(x, y):
    if x%y==0:
        return True
    else:
        return False

def range_sum(i, j):
    global nums
    _nums = nums[i:j+1]
    return sum(_nums)


for i in range(N):
    for j in range(i+1, N):
        total = range_sum(i, j)
        if mod(total, M):
            count += 1

    if mod(nums[i]*2, M):
        count += 1

print(count)