N = int(input())
nums = list(map(int,input().split()))
target = int(input())

# N = 9
# nums = [5,12,7,10,9,1,2,3,11]
# target = 13

count = 0

nums.sort()

start = 0
end = N-1

while start < end:
    if nums[start]+nums[end] == target:
        count += 1
        start += 1
        end -= 1
    elif nums[start]+nums[end] < target:
        start += 1
    else:
        end -= 1
        
print(count)