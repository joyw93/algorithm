arr = [("홍길동", 95), ("이순신", 77)]
result = []

sorted_arr = sorted(arr, key=lambda x: x[1])

for student in sorted_arr:
    result.append(student[0])

print(' '.join(result))