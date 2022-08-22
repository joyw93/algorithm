# 선택 정렬

array = [7,5,9,0,3,1,6,2,4,8]

N = len(array)


for i in range(N):
    for j in range(i+1, N):
        if array[j] < array[i]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            
print(array)
            