# N = int(input())
# nums = list(map(int, input().split()))

N = 4
nums = [3,5,2,7]

result = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        end = stack.pop()
        result[end] = nums[i]
    stack.append(i)
    
print(*result)
