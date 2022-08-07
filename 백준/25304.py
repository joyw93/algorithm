target = int(input())

N = int(input())

acc = 0
for i in range(N):
    data = list(map(int, input().split()))
    price = data[0]
    count = data[1]
    acc += price*count

if acc == target:
    print("YES")
else:
    print("NO")