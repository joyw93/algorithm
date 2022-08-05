N = int(input())
target = []
for i in range(N):
    target.append(int(input()))

stack = []
result = []
temp = 0

start = target[0]


for i in range(1, start+1):
    stack.append(i)
    result.append('+')
    temp = i

for number in target:
    if stack:
        current = stack[-1]
    else:
        current = 0

    if current > number:
        result = []
        break
    elif current == number:
        stack.pop()
        result.append('-')
    elif current < number:
        for i in range(temp+1, number+1):
            stack.append(i)
            result.append('+')
        temp = stack[-1]
        stack.pop()
        result.append('-')

if not result:
    print('NO')
else:
    for r in result:
        print(r)