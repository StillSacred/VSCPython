# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5.0, 10.01]
list3 = []
for i in range(len(list1)):
    if round((list1[i] - int(list1[i])), 2) != 0:
        list3.append(round((list1[i] - int(list1[i])), 2))
print(max(list3) -  min(list3))

# from random import randint
# nums = []
# for i in range(randint(5, 10)):
#     nums.append(round(randint(1,15) * 1.131, 2))
# print(nums, end=' -> ')
# nums = list(map(lambda x: round(x - int(x), 2), nums))
# print(max(nums) - min(nums))