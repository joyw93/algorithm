arr = [1,2,5,4,3]
brr = [5,5,6,6,5]

N = 5
K = 3
result = 0

arr = sorted(arr)
brr = sorted(brr, reverse=True)

for i in range(K):
    if arr[i] < brr[i]:
        arr[i], brr[i] = brr[i], arr[i]

print(arr)
print(brr)