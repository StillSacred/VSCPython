# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

arr = [1, 5, 2, 3, 4, 2, 6, 7, 4, 3, 2, 8, 9, 2, 1]

res = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        res.append(arr[i])
print(res)